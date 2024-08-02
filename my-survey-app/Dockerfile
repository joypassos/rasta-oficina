# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run the application
CMD ["python", "survey_app.py"]
