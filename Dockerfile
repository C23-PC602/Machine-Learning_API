FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update -y

RUN apt-get install unzip

RUN pip install python-multipart

RUN pip install gdown

RUN gdown 1eYca1OkvzTriyvr9qjGUGlyzxb-A3NMJ

RUN unzip model.zip

RUN rm model.zip

RUN pip install -r requirements.txt

CMD [ "python" , "main.py"]