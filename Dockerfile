FROM python:3.11.9-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && apt-get install -y netcat
RUN mkdir /app


COPY . ./app

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN sed -i 's/\r$//g' /app/build.sh
RUN chmod +x /app/build.sh

EXPOSE 8000

#ENTRYPOINT [ "gunicorn","test_django.wsgi" ]
ENTRYPOINT [ "/app/build.sh" ]
#ENTRYPOINT [ "python","manage.py","runserver" ]