# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Command to run tests
CMD ["python", "-m", "unittest", "test_insider.py"]



