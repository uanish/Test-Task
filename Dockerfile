FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install poetry==2.1.4
RUN poetry install --sync
RUN apt-get update && apt-get clean

