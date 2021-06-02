FROM python:3-buster

RUN pip3 install flask

COPY . /app

WORKDIR /app

CMD python3 flask_app.py