FROM python:3.6


RUN apt-get -y update
RUN pip3 install flask twilio

EXPOSE 80
ADD app.py /
ADD creds.py /
ADD truisms.csv /

CMD python3 app.py
