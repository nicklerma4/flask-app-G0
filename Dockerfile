#Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set up a working directory in /my_flask
WORKDIR /app

# Copy your Flask app into the working dir
COPY . /app

# Install any needed Python packages with pip 
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 avaiable to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]
