FROM python:3.13

WORKDIR usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY ./app .

CMD granian --interface asgi --reload --workers 2 --host 0.0.0.0 --port 8000 main:app
