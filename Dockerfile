# syntax=docker/dockerfile:1

FROM python:3.10-bullseye

WORKDIR .

COPY . /usr/src/crud_app

WORKDIR /usr/src/crud_app

RUN pip3 install -r /usr/src/crud_app/requirements.txt

CMD ["uvicorn", "app:app"]