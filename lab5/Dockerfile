FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
ADD ./app /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:80" ]