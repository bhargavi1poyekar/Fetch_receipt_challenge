# Using base image which includes python
FROM python:3.9-slim

# Sets working directory in container
WORKDIR /app

# Copy requirements.txt to container
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the python application
COPY app.py .

# Runs the flask app
CMD ["python", "-u", "app.py"]
