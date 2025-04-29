# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy the requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "demo:app", "--host", "0.0.0.0", "--port", "8000"]
