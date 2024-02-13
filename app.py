from flask import Flask, request, jsonify
import math
import uuid

app=Flask(__name__) # For web app



# (endpoint) Route for POST request
@app.route('/receipts/process', methods=['POST'])
def process_receipts():
	
	receipt_data =request.json # Get the json data from HTTP request
	
	# Call function to compute the points
	points=calculate_points(receipt_data)
	
	# Create an unique identifier 
	receipt_id =str(uuid.uuid4())
	
	# Store the id and points for further usage
	receipts[receipt_id]={'data':receipt_data, 'points':points}
	
	# Return id of the receipt
	return jsonify({'id':receipt_id})



# (endpoint) Route for GET request
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
	
	if receipt_id in receipts:
		# if valid receipt id return the calculated points
		return jsonify({'points':receipts[receipt_id]['points']})
	
	else:
		# return error
		return jsonify({'error':'Receipt ID not found'}), 404
	

# Function to compute points with the given rules
def calculate_points(receipt_data):

	points=0 # initial value
	
	# Rule 1: 1 point for every alphanum character in retailer name
	points+=sum(ch.isalnum() for ch in receipt_data['retailer'])
	
	
	# Rule 2: 50 points for round dollar total with no cents
	if receipt_data['total'].isdigit() or receipt_data['total'].endswith('.00'):
		# Checks whether an integer with no decimal or a decimal with .00 
		points+=50
		
		
	# Rule 3: 25 points if total multiple of 0.25
	if float(receipt_data['total']) % 0.25 == 0:
		points+=25
	
	# Rule 4: 5 points for every 2 items
	points+=len(receipt_data['items']) // 2 * 5
	
	
	# Rule 5: If trimmed length of desc of item multiple of 3, then round up of 0.2 times of price of item
	for item in receipt_data['items']:
	
		# trim the desc
		description_length=len(item['shortDescription'].strip())
		
		# check if multiple of 3
		if description_length % 3 == 0:
			
			# add points
			points+=math.ceil(float(item['price']) * 0.2)
			
	# Rule 6: 6 points for Odd Purchase Date 
	purchase_date=receipt_data['purchaseDate']
	if int(purchase_date.split('-')[2]) %2!=0:
		points+=6
	
	
	# Rule 7: 10 points for purchase time after 2 and before 4 pm
	if 14.00 < float('.'.join(receipt_data['purchaseTime'].split(':'))) < 16.00:
		points+=10
	
	# Return total points
	return points
	

if __name__ == '__main__':
	receipts = {} # in memory storage 
	
	# Define host and port to access the web service from outside the docker 
	app.run(host='0.0.0.0', port=5002, debug=True)
	
	
