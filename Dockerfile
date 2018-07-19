# Base
FROM python:3.6

# Author
MAINTAINER Bruce Tang <nicefish66@gmail.com>

# Environment Setup
RUN mkdir -p /workspace

WORKDIR /workspace
COPY . /workspace

RUN pip install -i https://pypi.douban.com/simple -r requirements.txt


ENV RUNENV Default


