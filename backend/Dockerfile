FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_ENV=prod \
    PORT=8080

WORKDIR /app

COPY backend/requirements.txt /tmp/backend-requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/backend-requirements.txt

COPY . /app

EXPOSE 8080

CMD ["sh", "-c", "uvicorn backend.stockarithm_api:app --host 0.0.0.0 --port ${PORT}"]
