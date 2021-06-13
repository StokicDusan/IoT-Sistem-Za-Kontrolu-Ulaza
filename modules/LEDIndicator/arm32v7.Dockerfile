FROM balenalib/raspberrypi3:stretch
WORKDIR /app

# disable python buffering to console out (https://docs.python.org/2/using/cmdline.html#envvar-PYTHONUNBUFFERED)
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN echo "deb http://deb.debian.org/debian jessie main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    python-pip \
    python-setuptools \
    swig \
    zlib1g-dev

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt \
    RPi.GPIO

ADD /app/ .
ADD /build/ .

ENTRYPOINT [ "python", "main.py" ]

