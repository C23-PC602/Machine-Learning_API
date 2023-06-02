FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update -y

RUN apt-get install unzip

RUN pip install gdown

RUN gdown 19laMMfY8zX8TM8Ni5N9lgDdcrANTsyyD

RUN unzip model.zip

RUN rm model.zip

RUN pip install -r requirements.txt

CMD [ "python" , "main.py"]