FROM python:alpine

RUN pip install Flask

WORKDIR /app

COPY app.py ./

ENV FLASK_APP app.py

CMD flask run --host=0.0.0.0
