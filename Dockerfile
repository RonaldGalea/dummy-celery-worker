# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory (with your tasks.py) into the container
COPY . /app/

# Command to run the Celery worker
CMD ["celery", "-A", "example-name", "worker", "--loglevel=info", "--config=celeryconfig"]
