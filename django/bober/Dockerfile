# vim:set ft=dockerfile:
FROM debian:testing
LABEL maintainer="Gregor Jerše <gregor.jerse@fri.uni-lj.si>"

ENV BOBER_GIT_LOCATION=https://github.com/polz113/bober.git
ENV BOBER_GIT_BRANCH=master

# Secret key is only here to make collectstatic work.
# It is overrided from settings in docker-compose.
ENV SECRET_KEY=very_secret_key

# Add user and group bober first to make sure their IDs get assigned consistently
RUN groupadd -r bober && useradd -r -g bober bober

# Change locale to en_US.UTF-8
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
    
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8 

# Install required packages
RUN apt-get update \
  && apt-get install -y \
  uwsgi \
  uwsgi-plugin-python3 \
  python3 \
  python3-pip \
  git \
  postgresql-server-dev-all \
  libpython3-dev \
  libsasl2-dev \
  libldap2-dev \
  unixodbc-dev \
  python3-cairo \
  python3-lxml \
  python3-psycopg2 \
  default-libmysqlclient-dev \
  gettext \
   && rm -rf /var/lib/apt/lists/*

WORKDIR /home/bober

# Pull tomo source into current working directory
# RUN git clone --depth 1 -b ${BOBER_GIT_BRANCH} ${BOBER_GIT_LOCATION}

# Copy the current source code inside docker container
COPY --chown=bober:bober . bober/
RUN ls /home/bober
RUN ls /home/bober/bober
RUN pwd
RUN ls .

# Install dependencies
RUN pip3 install -r requirements-docker.txt

# Compile translations
RUN manage.py compilemessages --settings=bober.settings-docker

RUN chown bober.bober -R /home/bober

# UWSGI options are read from environmental variables.
# They are specified in docker-compose file.
CMD ["uwsgi"]
