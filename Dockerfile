FROM python:3.9

WORKDIR /usr/src/app/standoffbot

COPY requirements.txt /usr/src/app/standoffbot
RUN pip install -r /usr/src/app/standoffbot/requirements.txt
COPY . /usr/src/app/standoffbot

CMD python3 -m bot