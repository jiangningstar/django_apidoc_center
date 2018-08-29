############################################################

# Dockerfile to build django_apidoc_center Installed Containers

# based on Ubuntu

# VERSION 1

#############################################################

# set the base image to ubuntu
FROM ubuntu:14.04

COPY sources.list /etc/apt/sources.list

RUN apt-get clean && apt-get update && apt-get install -y python-dev && apt-get install -y python-pip && apt-get install -y libjpeg-dev && apt-get install -y nginx && apt-get install -y libmysqlclient-dev && apt-get install -y vim

ADD ./requirements /requirements

RUN sudo pip install --upgrade -i http://mirrors.aliyun.com/pypi/simple pip
RUN sudo pip install --no-cache-dir -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r /requirements/production.txt

RUN sudo echo "Asia/Shanghai" > /etc/timezone

# Setup nginx
COPY ./conf/nginx.conf /etc/nginx/sites-enabled/default
RUN echo 'daemon off;' >> /etc/nginx/nginx.conf

## Supervisor
RUN sudo apt-get install -y supervisor && \
    sudo apt-get clean && \
    mkdir -p /linkedsee/logs/supervisord/

RUN mkdir -p /data/logs/linkedsee/

EXPOSE 8000

ADD ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD . /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
