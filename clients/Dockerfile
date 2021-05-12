FROM python:3.8-slim

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app

ENTRYPOINT python3 -u main.py
