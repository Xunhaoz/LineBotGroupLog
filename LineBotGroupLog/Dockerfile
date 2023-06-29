FROM python:3.9 

COPY ./requirements.txt /app
WORKDIR /app

RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]

