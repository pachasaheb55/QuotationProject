# Dockerfile

# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt