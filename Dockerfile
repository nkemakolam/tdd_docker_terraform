# pull official base image
FROM python:3.7.4-alpine

# set working directory
RUN mkdir -p /usr/src/app


# new
# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# new
# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
# add app
COPY . /usr/src/app
# run server
#CMD python manage.py run -h 0.0.0.0