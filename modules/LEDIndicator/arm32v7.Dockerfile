FROM balenalib/raspberrypi3:stretch

RUN [ "cross-build-start" ]

ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN echo "deb http://deb.debian.org/debian jessie main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    python-pip \
    python-setuptools \
    swig \
    zlib1g-dev\
    libopenjp2-7-dev \
    libatlas-base-dev \
    wget \
    libboost-python1.62.0 \
    curl \
    libcurl4-openssl-dev

COPY /build/arm32v7-requirements.txt ./
RUN pip install --upgrade pip 
RUN pip install --upgrade setuptools
RUN pip install -r arm32v7-requirements.txt

RUN [ "cross-build-end" ]

ADD /app/ .
ADD /build/ .

ENTRYPOINT [ "python", "main.py" ]

