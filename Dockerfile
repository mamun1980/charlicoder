FROM python:3.9.6-slim-buster

ARG APPUSER=charlicoder
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update -y 
# && apt-get install -y sudo 
# DEBIAN_FRONTEND=noninteractive \
# apt-get install -y --no-install-recommends apt-utils build-essential sudo 
RUN useradd -m ${APPUSER} 
# && usermod -aG sudo ${APPUSER}

USER ${APPUSER}
ENV PATH /home/${APPUSER}/.local/bin:$PATH
RUN mkdir -p /home/${APPUSER}/app
WORKDIR /home/${APPUSER}/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt