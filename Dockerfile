FROM python:3.8-alpine

RUN mkdir /server/

ADD src/server.py /server/

WORKDIR /server/

COPY src .

COPY requirements.txt /server/

RUN set -x && \
    pip install --no-cache-dir --disable-pip-version-check --upgrade pip && \
    pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

EXPOSE "8080"
