# Use an official Python runtime as a parent image
FROM python:3.11-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Create a directory for NLTK data
RUN mkdir -p /app/resources 

# Install wget
RUN apt-get update && apt-get install -y wget

# Download the model
RUN wget -O app/models/lid.176.bin https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]
