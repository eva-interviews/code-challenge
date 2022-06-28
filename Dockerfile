FROM python:3.8 AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip3 install --upgrade pip

WORKDIR /core

COPY . /core

RUN pip install -r requirements.txt

ENTRYPOINT ["python","manage.py", "runserver", "0.0.0.0:8000"]
