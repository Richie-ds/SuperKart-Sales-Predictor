
# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7860 for the Flask application
EXPOSE 7860

# Run the application using Gunicorn
CMD exec gunicorn --bind :7860 --workers 1 --threads 8 --timeout 0 app:app
