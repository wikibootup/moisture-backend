FROM python:3.5
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
RUN pip3 install -U pip setuptools

RUN pip install -r requirements.txt
