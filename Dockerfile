FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# Expose port 5000 (for Flask) and port 27017 (for MongoDB)
EXPOSE 5000
EXPOSE 27017

# Set the Flask application entry point
ENV FLASK_APP=app

# Command to run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]
