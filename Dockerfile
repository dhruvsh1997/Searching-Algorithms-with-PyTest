# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files (excluding env, etc. via .dockerignore)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir pytest

# Run tests by default
CMD ["pytest"]