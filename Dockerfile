FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install unzip 

RUN pip install python-multipart

RUN pip install gdown

RUN gdown 1eYca1OkvzTriyvr9qjGUGlyzxb-A3NMJ

RUN unzip model.zip

RUN rm model.zip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD uvicorn main:app --host 0.0.0.0 --port 8080


