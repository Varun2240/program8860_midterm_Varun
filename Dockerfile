# Use Python 3.9 base image
FROM python:3.9-slim

WORKDIR /app

# Copy requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run your application
CMD ["python", "todo/app.py"]
