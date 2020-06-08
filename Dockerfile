FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -



RUN apt-get install -y apt-utils
RUN apt-get install -y  nodejs

WORKDIR /CPL



COPY . /CPL
RUN pip3 install -r requirements.txt
RUN npm install
RUN npm run dev

ENV FLASK_APP="application.py"
ENV FLASK_ENV="development"
ENV LC_ALL="C.UTF-8"
ENV LANG="C.UTF-8"


CMD flask run --host 0.0.0.0
