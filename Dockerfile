FROM python:3.9.9

RUN apt-get update &&\
    apt-get install -y git sudo curl

RUN useradd -m jupyter &&\
    echo "jupyter:jupyter" | chpasswd &&\
    adduser jupyter sudo
USER jupyter

ARG HOME_DIR=/home/jupyter
RUN  mkdir -p ${HOME_DIR}/.local/bin
WORKDIR ${HOME_DIR}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH ${PATH}:${HOME_DIR}/.poetry/bin
RUN . ~/.bashrc

ENV SHELL /bin/bash
