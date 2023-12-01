# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY ["ping.py", "requirements.txt", "./"]
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY "ping.py" .

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "ping:app"]