 # Use the official Python base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY app .

# Expose the port on which the Gunicorn server will run
EXPOSE 8000

WORKDIR /
# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.startup:app"]
