#      _    ___      _                _ _           _   _             
#     / \  |_ _|    / \   _ __  _ __ | (_) ___ __ _| |_(_) ___  _ __  
#    / _ \  | |    / _ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \ 
#   / ___ \ | |   / ___ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | |
#  /_/   \_\___| /_/   \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|
#                        |_|   |_|                                    

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

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
