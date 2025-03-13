FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir Flask==2.3.3 Werkzeug==2.3.7 gunicorn==21.2.0

RUN useradd -m gunicorn

RUN chown -R gunicorn:gunicorn /app
USER gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--timeout", "120", "app:app"]

EXPOSE 5000