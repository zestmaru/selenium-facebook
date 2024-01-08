# syntax=docker/dockerfile:1
FROM python:3.10-alpine 

WORKDIR /app
COPY requirements.txt /app
COPY config.cfg /app
RUN pip install -r requirements.txt

COPY . /app

# chromedriver
RUN apk update && apk add --no-cache bash \
        chromium \
        chromium-chromedriver

EXPOSE 5000

ENV FLASK_APP=flask-app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
