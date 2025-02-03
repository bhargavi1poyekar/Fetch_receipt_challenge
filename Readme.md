# Fetch Receipt Processor Challenge
Bhargavi Poyekar - bpoyeka1@umbc.edu

## Instructions to run the web service

### Introduction:

This project provides a web service for submitting and viewing receipt data via a formal API, as described in the api.yml file. The API allows users to submit receipt information, and retrieve associated points. In addition to the API, a simple user interface (UI) has been added for submitting and viewing receipts and the respective points.

### Commands to run:

Clone github project:

    git clone https://github.com/yourusername/fetch-receipt-system.git
    cd fetch-receipt-system

Once you clone the github project, run the following commands:

Assuming that you have docker installed:

1. Build the docker image as per requirements in dockerfile 
    
        docker build -t receipt-processor .  


2. Runs the docker with name recpt by mapping port 5002 of host machine with containers port 5002.

        docker run --name recpt -d -p 5002:5002 receipt-processor

    Note: If you want to change the port number, you need to edit the app.py last line, port number and then rerun the above 2 commands. This is because, I have included the line there to access the localhost of docker from host machines, so you don't need to enter the docker for testing. 

3. Send POST request with valid_rpt1.json as input receipt.     
    
        curl -X POST -H "Content-Type: application/json" -d @test_receipts/valid_rpt1.json http://localhost:5002/receipts/process


4. Send GET request to the service with receipt id. X being the receipt ID that you received in previous post request.  
 
        curl -X GET http://localhost:5002/receipts/{X}/points

### Project Structure:

- app
    - controllers
        - receipt_controller.py: sets up routes in a web application to display forms, process receipt data, and get details or points for a receipt through API calls.
    - services
        - receipt_service.py: functions to process receipts, calculate points based on various criteria, and store and retrieve receipt details in memory using a unique receipt ID.
    - templates
        - receipt_form.html: allows users to submit receipt JSON data, displays the generated receipt ID upon success
        - receipt_view.html: allows users to input a receipt ID, view detailed information about the receipt (including retailer, purchase date, time, total, and items), and fetch points associated with the receipt
    - schemas.py:defines Marshmallow schemas for validating receipt and item data.
- test_receipts
    - valid_rpts.json (1-4): Json examples for valid receipts. 
    - invalid_rpts.json(1-8): Json examples for invalid receipts. 
- tests:
    - test_receipt_controller.py: unit tests for receipt processing, validation, and retrieval endpoints correctness and error handling.
    - test_receipt_service.py: Unit tests for receipt service functions, verifying point calculation and unique receipt ID generation.
 
### Features
1. Submit Receipt: Users can submit receipt data in JSON format.
2. View Receipt: Users can retrieve the details of a receipt by its ID.
3. Get Points: Users can fetch the points associated with a receipt.
4. User Interface (UI): Provides a simple web interface to interact with the API for submitting and viewing receipts.
5. API Testing: You can test the API using curl commands.



### API Endpoints:

1. Submit Receipt

    URL: /receipts/process

    Method: POST

    Description: Submit a receipt in JSON format to the server.

    Request Body Example:

        {
            "retailer": "Walgreens",
            "purchaseDate": "2022-01-02",
            "purchaseTime": "08:13",
            "total": "2.65",
            "items": [
                {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
                {"shortDescription": "Dasani", "price": "1.40"}
            ]
        }

    Response:  

        {
            "id": "5b62ba8e-5488-44d5-9f18-043d20deae03"
        } 
    
2. Get Points
    
    URL: /receipts/{receiptId}/points
    
    Method: GET
    
    Description: Retrieve the points associated with a receipt by its ID.
    
    Response:

        {
            "points": 10
        }


### Technologies Used
1. Backend: Flask (Python web framework) for the web service and API logic.
2. Frontend: HTML, CSS, and JavaScript for the UI.
3. Containerization: Docker for easy deployment.



### Unit Tests

Invalid test receipts:

1. The price uses a comma (6,49) instead of a period (6.49).
2. The items array is empty, but it is required to have at least one item.
3. The retailer name contains the @ symbol, which is not allowed.
4. The purchaseDate has an invalid month.
5. The purchaseTime field contains an invalid hour.
6. The total has only one decimal place (6.4 instead of 6.40).
7. The shortDescription for the item is an empty string, which is not allowed.
8. The items array contains an item with no price.




