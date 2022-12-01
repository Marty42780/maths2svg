FROM ubuntu

# copy project
COPY . /usr/src/app/

# set work directory
WORKDIR /usr/src/app/

# install dependencies
RUN apt-get update \
  && apt-get install -y libcairo2-dev \
  && apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir Maths2SVG/results

EXPOSE 80
ENTRYPOINT gunicorn app:app -w 2 --threads 3 -b 0.0.0.0:80
