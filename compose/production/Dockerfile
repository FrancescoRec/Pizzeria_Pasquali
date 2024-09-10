# Production Dockerfile using Python 3.11
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker layer caching
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files to the working directory
COPY . /app

# Expose the port the app will run on
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run production server with production settings
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=Pizzeria_Pasquali.settings.production"]
