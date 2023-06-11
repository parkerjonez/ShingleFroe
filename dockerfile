# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Install git and git-lfs
RUN apt-get update && \
    apt-get install -y git git-lfs && \
    git lfs install

# Add the current directory contents into the container at /app
ADD . /app

# Pull the large files
RUN git lfs pull

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]
