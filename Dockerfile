FROM python:3.10.3-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install unzip 

RUN pip install python-multipart

RUN pip install gdown

RUN gdown 1L3zBe8W1mKXgjFLN3ZwsJz3rHOJ7YtN4

RUN unzip model-v2.zip

RUN rm model-v2.zip

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED True

CMD ["python", "main.py"]


