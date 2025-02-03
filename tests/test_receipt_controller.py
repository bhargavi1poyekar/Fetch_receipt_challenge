import unittest
import json
import os
from app import create_app

class ReceiptTestCase(unittest.TestCase):

    def setUp(self):
        # Create a Flask test client
        self.app = create_app()
        self.client = self.app.test_client()

    def load_receipt_from_file(self, filename):
        # Helper function to load receipt JSON from a file in the project directory.
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'test_receipts', filename)
        with open(file_path, 'r') as file:
            return json.load(file)

    def test_process_receipt_valid(self):
        valid_receipt = self.load_receipt_from_file('valid_rpt1.json')

        # Send POST request with valid receipt
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(valid_receipt),
                                    content_type='application/json')

        # Check that the response status is 201 Created
        self.assertEqual(response.status_code, 201)
        response_json = response.get_json()
        self.assertIn('id', response_json)

    def test_process_receipt_invalid_price(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt1.json')

        # Send POST request with invalid receipt
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')

        # Check that the response status is 400 Bad Request
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)


    def test_process_receipt_invalid_items(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt2.json')

        # Send POST request with invalid receipt
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')

        # Check that the response status is 400 Bad Request
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)


    def test_process_receipt_invalid_retailer(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt3.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)
    

    def test_process_receipt_invalid_date(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt4.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)

    
    def test_process_receipt_invalid_time(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt5.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)


    def test_process_receipt_invalid_total(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt6.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)

    
    def test_process_receipt_invalid_short_desc(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt7.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)

    
    def test_process_receipt_invalid_item_price(self):
        invalid_receipt = self.load_receipt_from_file('invalid_rpt8.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(invalid_receipt),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        response_json = response.get_json()
        self.assertIn('error', response_json)
        self.assertIn('details', response_json)


    def test_get_points_valid(self):
        valid_receipt = self.load_receipt_from_file('valid_rpt1.json')

        # Send POST request to process receipt
        post_response = self.client.post('/receipts/process', 
                                         data=json.dumps(valid_receipt),
                                         content_type='application/json')
        post_response_json = post_response.get_json()
        receipt_id = post_response_json['id']

        # Send GET request to fetch points
        response = self.client.get(f'/receipts/{receipt_id}/points')

        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the response contains points
        response_json = response.get_json()
        self.assertIn('points', response_json)

    def test_get_points_invalid(self):
        # Send GET request with invalid receipt id
        response = self.client.get('/receipts/invalid_receipt_id/points')

        # Check that the response status is 404 Not Found
        self.assertEqual(response.status_code, 404)

        # Check if error message is returned
        response_json = response.get_json()
        self.assertIn('error', response_json)

    def test_get_receipt_details_valid(self):
        receipt_data = self.load_receipt_from_file('valid_rpt1.json')
        response = self.client.post('/receipts/process', 
                                    data=json.dumps(receipt_data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)
        
        # Get the receipt_id from the response after submission
        response_json = json.loads(response.data)
        receipt_id = response_json['id'] 
        
        response = self.client.get(f'/receipts/{receipt_id}/details')
        
        # Check if the response is valid
        self.assertEqual(response.status_code, 200)
        
        # Check that the response JSON matches the expected structure
        response_json = json.loads(response.data)
    
        self.assertEqual(response_json['receipt']['retailer'], receipt_data['retailer'])
        self.assertEqual(response_json['receipt']['total'], receipt_data['total'])
        self.assertEqual(response_json['receipt']['purchaseDate'], receipt_data['purchaseDate'])
        self.assertEqual(response_json['receipt']['purchaseTime'], receipt_data['purchaseTime'])

    def test_get_receipt_details_invalid(self):
        """Test the '/receipts/<receipt_id>/details' route with an invalid receipt ID."""
        invalid_receipt_id = "invalid_id"
        
        # Send a GET request with an invalid ID
        response = self.client.get(f'/receipts/{invalid_receipt_id}/details')
        
        # Assert that the response is a 404
        self.assertEqual(response.status_code, 404)
        response_json = json.loads(response.data)
        self.assertEqual(response_json['error'], 'Receipt ID not found')
