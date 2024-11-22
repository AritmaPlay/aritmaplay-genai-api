# Use a Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt --index-url https://pypi.org/simple/

# Copy the rest of the application files into the container
COPY . /app/

# Set the environment variable for GCP credentials
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/try-vertexai-441706-3ccd7445630d.json

# Expose the port the app runs on
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
