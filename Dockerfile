FROM python:3.8.0

MAINTAINER tackie

ENV USER tackie
ENV HOME /home/${USER}
ENV SHELL /bin/bash

RUN useradd -m ${USER}
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:tackie" | chpasswd

RUN echo "alias ll='ls -l'" >> /${HOME}/.bashrc

RUN apt-get update \
    && apt-get upgrade -y \
    # image のサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # pip アップデート
    && pip install --upgrade pip

WORKDIR /home/python/modules
COPY requirement ${PWD}

RUN pip install -r requirement

WORKDIR /home/python/src

