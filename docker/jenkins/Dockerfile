FROM jenkins:1.585

MAINTAINER Gavin Noronha <gavinln@hotmail.com>

USER root

# Python binary dependencies, developer tools
RUN apt-get update && apt-get install -y -q \
    python \
    python-pip

RUN pip install pep8

# setup plugins
COPY plugins.sh /usr/share/jenkins/plugins.sh
COPY plugins.txt /plugins.txt

RUN /usr/share/jenkins/plugins.sh

USER jenkins
