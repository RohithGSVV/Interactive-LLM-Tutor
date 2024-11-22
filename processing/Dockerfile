#   ____                              _             
#  |  _ \ _ __ ___   ___ ___  ___ ___(_)_ __   __ _ 
#  | |_) | '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
#  |  __/| | | (_) | (_|  __/\__ \__ \ | | | | (_| |
#  |_|   |_|  \___/ \___\___||___/___/_|_| |_|\__, |
#                                             |___/ 
# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

