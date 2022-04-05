FROM python:3.9.9

RUN apt-get update &&\
    apt-get install git &&\
    apt-get install sudo

RUN useradd -m jupyter &&\
    echo "jupyter:jupyter" | chpasswd &&\
    adduser jupyter sudo
USER jupyter

RUN  mkdir -p /home/jupyter/.local/bin
WORKDIR /home/jupyter

COPY requirements.txt .
ENV PATH ${PATH}:/home/jupyter/.local/bin
RUN python -m pip install --upgrade pip setuptools &&\
    python -m pip install --user -r requirements.txt &&\
    rm requirements.txt

ENV SHELL /bin/bash
