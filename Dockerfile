FROM python:3.9

RUN apt-get update -qq \
    && apt-get -yqq install git tini   > /dev/null 

EXPOSE 8000

## Install Buildbot 
ADD requirements.txt /tmp/
RUN python -m pip install uwsgi
RUN pip install -r /tmp/requirements.txt

## Add other files
ADD docker/uwsgi.ini  /app/
ADD docker/docker-entrypoint.sh /

ADD core /app/escapes-web/core
ADD static /app/escapes-web/static
ADD templates /app/escapes-web/templates
ADD escapes /app/escapes-web/escapes
ADD escapes_api /app/escapes-web/escapes_api

ADD manage.py /app/escapes-web/manage.py

WORKDIR /app
ENTRYPOINT ["tini", "--"]
CMD ["/bin/bash", "/docker-entrypoint.sh"]