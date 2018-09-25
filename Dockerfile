FROM python:3.6-alpine

RUN apk add --update \
	gcc \
	libffi-dev \
	musl-dev \
	make

RUN pip install --upgrade pip

COPY dev-requirements.txt /
RUN pip install -r dev-requirements.txt
