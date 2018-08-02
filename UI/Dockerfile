FROM ubuntu:16.04
MAINTAINER ugur cekmez <ugur.cekmez@tubiotak.gov.tr>


RUN apt-get update && apt-get install -y curl git

# Install latest nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y --no-install-recommends \
  nodejs       \
  build-essential \
  unzip

RUN npm install -g serve

COPY ./ui /ui
WORKDIR /ui

RUN npm install
RUN npm run build

EXPOSE 7779

ENTRYPOINT serve -s build --listen 7779


# EOF
