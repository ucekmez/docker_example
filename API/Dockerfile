FROM ubuntu:16.04
MAINTAINER ugur cekmez <ugur.cekmez@tubitak.gov.tr>

# Install system-wide packages
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        wget \
        vim \
        git \
        python3-setuptools \
        python3.5 \
        python3.5-dev \
        ca-certificates


# Make python3 default
RUN ln -s -f /usr/bin/python3 /usr/bin/python

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm get-pip.py

COPY ./api /api
WORKDIR /api

RUN pip install --no-cache -r requirements.txt --upgrade

EXPOSE 7778

CMD gunicorn -b 0.0.0.0:7778 --reload API




# EOF
