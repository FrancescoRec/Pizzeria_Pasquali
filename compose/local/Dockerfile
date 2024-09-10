# Local development Dockerfile using Python 3.11
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy local requirements file to the container
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project directory to the container
COPY . /app

# Expose the port the Django app runs on
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=Pizzeria_Pasquali.settings.local"]
