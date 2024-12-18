# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Define environment variable
ENV GOOGLE_APPLICATION_CREDENTIALS="/secrets/capstone-c242-ps102-592cd9da967c.json"

# Run app.py when the container launches
CMD ["python", "motivational_genai.py"]
