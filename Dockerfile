# Use the official Python image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy requirements file first (for better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
# EXPOSE 8000
EXPOSE $PORT

# Command to run the application
# CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8000"]
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"] 
