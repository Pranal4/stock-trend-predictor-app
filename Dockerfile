# Dockerfile for our Stock Predictor API

# 1. Start from an official Python base image.
FROM python:3.9-slim

# 2. Set the working directory inside the container.
WORKDIR /app

# 3. Copy the requirements file into the container first.
COPY requirements.txt .

# 4. Install the Python dependencies from the requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our application's code into the container.
COPY . .

# 6. Expose the port that our FastAPI application will run on.
EXPOSE 8000

# This is the NEW CMD line for the end of your Dockerfile
CMD ["python", "main.py"]