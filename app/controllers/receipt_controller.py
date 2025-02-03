from flask import Blueprint, request, jsonify, render_template
from app.services.receipt_service import process_receipt, get_receipt_points, get_receipt_details
from app.schemas import ReceiptSchema

receipt_bp = Blueprint('receipt', __name__)

# Route for Receipt Submission.
@receipt_bp.route('/receipts/form', methods=['GET'])
def get_receipt_form():
    return render_template('receipt_form.html')


# Route for Viewing Receipt and its points. 
@receipt_bp.route('/receipts/view', methods=['GET'])
def view_receipt_page():
    return render_template('receipt_view.html')


# Receipt Processing Endpoint
@receipt_bp.route('/receipts/process', methods=['POST'])
def process_receipts():
    receipt_data = request.json  
    
    # Validate the receipt data using Marshmallow schema. 
    receipt_schema = ReceiptSchema()
    errors = receipt_schema.validate(receipt_data)
    
    if errors:
        # Return error, incase of invalid receipt. 
        return jsonify({"error": "Invalid receipt data", "details": errors}), 400

    # Call function to process the receipt
    receipt_id = process_receipt(receipt_data)
    
    # Return the receipt ID
    return jsonify({'id': receipt_id}), 201


# Get Receipt Points Endpoint
@receipt_bp.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):

    # Call function to get receipt points
    points = get_receipt_points(receipt_id)
    
    # Return points
    if points is not None:
        return jsonify({'points': points})
    else:
        return jsonify({'error': 'Receipt ID not found'}), 404


# Get Receipt Details 
@receipt_bp.route('/receipts/<receipt_id>/details', methods=['GET'])
def get_receipt(receipt_id):

    # Call function to get receipt points
    receipt_details = get_receipt_details(receipt_id)

    # Return receipt details.
    if receipt_details:
        return jsonify(receipt_details)
    else:
        return jsonify({'error': 'Receipt ID not found'}), 404


