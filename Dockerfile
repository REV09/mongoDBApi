FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip3 install -r requeriments.txt
