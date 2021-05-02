#FROM ubuntu:18.04
FROM python:3.8

MAINTAINER Tyler Balson <tbalson@iu.edu>

ENV DEBIAN_FRONTEND=noninteractive

#RUN git clone https://github.com/tbalson/cpu_test.git

WORKDIR cpu_test/
COPY . /cpu_test

#RUN git pull

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["make", "start"]
