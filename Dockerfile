# Dockerfile for Selenium tests

# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test scripts
COPY . .

# Command to run the tests
CMD ["python", "run_tests.py"]
