FROM python:3.10.6-alpine3.16

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN  apt-get update \
  && apt-get install -y libcairo2-dev
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/run.sh"]