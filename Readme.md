# Fetch Receipt Processor Challenge
Bhargavi Poyekar - bpoyeka1@umbc.edu

## Instructions to run the web service

### Introduction:

I have used Python Flask to complete this challenge. To avoid any problems related to dependencies, I have used docker and provided dockerfile to build image and run the container. I have also uploaded the examples that you provided for testing as json files. For testing purposes I used curl to send requests to the http server. 

### Contents:

1. app.py -> python (flask file with the code).
2. requirements.txt -> with the required dependencies.
3. Dockerfile -> to build the docker image. 
4. e1.json, e2.json, e3.json, e4.json -> your given examples.

### Commands to run:

Once you download all the above files (make sure that they are all in the same directory), run the following commands:

Assuming that you have docker installed:

1. docker build -t receipt-processor .  
=> Builds the docker image as per requirements in dockerfile

2. docker run --name recpt -d -p 5002:5002 receipt-processor
=> Runs the docker with name recpt by mapping port 5002 of host machine with containers port 5002.

Note: If you want to change the port number, you need to edit the app.py last line, port number and then rerun the above 2 commands. This is because, I have included the line there to access the localhost of docker from host machines, so you don't need to enter the docker for testing. 

3. curl -X POST -H "Content-Type: application/json" -d @e1.json http://localhost:5002/receipts/process
=> Send POST request with e1.json as input receipt.

4. curl -X GET http://localhost:5002/receipts/{enter the id you receive in post here}/points
=> Send GET request to the service with receipt id.

### Conclusion:

This was a small challenge yet I learned many new things from it and I would like to thank 'Fetch' for giving me this opportunity. I would like to summarize my learnings. 

1. I've gained valuable insights into the power of Docker in maintaining consistent environments across different devices. I've learned how to create Docker images using Dockerfiles, enabling me to encapsulate my application and its dependencies.

2. Furthermore, I've enhanced my troubleshooting skills by mastering commands like docker logs and docker ps, which have proven invaluable in debugging container issues and managing container instances efficiently.

3. This experience has also provided me with an opportunity to revisit and reinforce my understanding of Flask and HTTP requests, reaffirming their importance in modern web development.

4. Overall, this challenge has been a rewarding learning experience, equipping me with practical skills and knowledge that I can apply in future projects.







