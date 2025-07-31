# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port (Django runs on 8000 by default)
EXPOSE 8000

# Run migrations and start the dev server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
