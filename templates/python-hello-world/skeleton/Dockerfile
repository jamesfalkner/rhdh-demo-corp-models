FROM python:3.11-slim

WORKDIR /app

# Copy application files
COPY app.py .
COPY requirements.txt .
COPY templates/ ./templates/
COPY static/ ./static/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Set environment variable for port
ENV PORT=8080

# Run the application
CMD ["python", "app.py"]

