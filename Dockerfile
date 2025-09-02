# 1) Base image with Python
FROM python:3.11-slim

# 2) Work inside /app
WORKDIR /app

# 3) Helpful Python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4) Install Python deps
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5) Copy your project code
COPY . /app/

# 6) Default command (production-style)
#    Gunicorn runs Django in a fast server
CMD ["gunicorn", "synestra.wsgi:application", "--bind", "0.0.0.0:8000"]
