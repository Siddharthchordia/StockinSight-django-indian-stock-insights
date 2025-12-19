FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN addgroup --system django && adduser --system --ingroup django django

# Copy project files
COPY . .

# Create static directory (important for collectstatic)
RUN mkdir -p /app/staticfiles && chown -R django:django /app

USER django

EXPOSE 8000
