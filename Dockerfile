FROM python:3.11-slim

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
