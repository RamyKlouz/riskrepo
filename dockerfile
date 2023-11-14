# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the project code to the container
COPY . /app

# Install the project dependencies
RUN pip install -r requirements.txt

# Expose the port that Django runs on
EXPOSE 8000

# Specify the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
