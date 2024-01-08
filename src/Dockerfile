# syntax=docker/dockerfile:1
FROM python:3.10-alpine 

WORKDIR /app
COPY . /app

RUN apk update && apk add --no-cache bash \
        gcc \
        musl-dev \
        linux-headers \
        libffi-dev \
        chromium \
        chromium-chromedriver

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=flask-app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
