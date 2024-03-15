# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run linting checks
RUN pylint src/*.py

# Run unit tests
RUN python -m unittest src/test_find_matching_pair.py

# Define the command to run the script when the container starts
CMD ["python", "./src/find_matching_pair.py"]
