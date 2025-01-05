# Use the official Python base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies for Playwright
RUN apt-get update && apt-get install -y \
    curl \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libgbm-dev \
    libcups2 \
    libxkbcommon0 \
    libgtk-3-0 \
    wget \
    && apt-get clean

# Install Playwright and dependencies
RUN pip install --no-cache-dir playwright && playwright install

RUN playwright install-deps

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI app port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
