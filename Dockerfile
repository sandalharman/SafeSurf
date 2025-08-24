# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# FastAPI + dependencies
RUN pip install fastapi uvicorn httpx

# Copy the app
COPY ./app /app/app
COPY ./config /app/config
COPY ./models /app/models

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
