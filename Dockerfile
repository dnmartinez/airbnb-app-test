# Use an official Python runtime as an image
FROM python:3.8

# set a directory for the app
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD python app.py



