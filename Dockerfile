FROM python:3.10.6-alpine3.16

# copy project
COPY . /usr/src/app/

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN apk add cairo
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT gunicorn app:app -w 2 --threads 3 -b 0.0.0.0:80