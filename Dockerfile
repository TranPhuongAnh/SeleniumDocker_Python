# Base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test code
COPY src/ ./src/

# Default command to run the test
CMD ["python", "src/main/run/main.py"]