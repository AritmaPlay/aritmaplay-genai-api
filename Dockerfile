# Use a Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt --index-url https://pypi.org/simple/

# Copy application files into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8080

# Run the app with Gunicorn for production
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
