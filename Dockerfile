FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY oas.yaml oas.yaml
COPY waitlist waitlist
COPY src src
WORKDIR /src