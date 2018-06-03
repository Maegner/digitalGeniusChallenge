# Use an official Python runtime as a parent image
FROM ubuntu:latest

#geting python3 and pip3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Set the working directory to /digital_genius
WORKDIR /digital_genius

# Copy the current directory contents into the container at /digital_genius
ADD . /digital_genius

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME DigitalGenius

# Run app.py when the container launches
CMD ["python3", "app.py"]
