FROM python:3.11-slim

# Add system dependencies for pycairo/weasyprint

RUN apt-get update && apt-get install -y \
    gcc \
    libcairo2 \
    libcairo2-dev \
    libpango1.0-dev \
    libgdk-pixbuf2.0-dev \
    libffi-dev \
    shared-mime-info

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/


# Default command
CMD ["gunicorn", "erp_1_0.wsgi:application", "--bind", "0.0.0.0:8000"]

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /code/


# Default command
CMD ["gunicorn", "erp_1_0.wsgi:application", "--bind", "0.0.0.0:8000"]
