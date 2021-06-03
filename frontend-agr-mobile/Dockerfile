FROM tiangolo/uvicorn-gunicorn:python3.8

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1