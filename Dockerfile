FROM python:3

RUN mkdir /clavesredproteccionsocial

WORKDIR /clavesredproteccionsocial

COPY requirements.txt /clavesredproteccionsocial

RUN pip install -r requirements.txt

COPY . /clavesredproteccionsocial

CMD [ "python", "./bot.py" ]