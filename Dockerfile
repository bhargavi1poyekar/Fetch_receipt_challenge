# Using base image which includes python
FROM python:3.9-slim

# Sets working directory in container
WORKDIR /app

# Copy everything in the curr directory to container
COPY . .

# Install the required libraries
RUN pip install -r requirements.txt

EXPOSE 5002
# Runs the flask app
CMD ["python", "-u", "run.py"]
