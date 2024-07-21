# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy test scripts
COPY . .

# Command to run tests
CMD ["pytest", "tests/"]
