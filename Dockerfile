FROM python:3.9.9

RUN apt-get install git

COPY requirements.txt .
RUN pip install --upgrade pip setuptools &&\
    pip install -r requirements.txt

RUN useradd -m jupyter
USER jupyter

RUN mkdir /home/jupyter/data
WORKDIR /home/jupyter