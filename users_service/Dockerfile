FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install debugpy

# Copy the application code
COPY . .

# Expose necessary ports
EXPOSE 8000 5678

# Enable debugpy via environment variable
ENV DEBUGPY_ENABLE=true

# Start the application with uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
