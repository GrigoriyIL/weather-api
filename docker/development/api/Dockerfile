FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/app/web

RUN pip install --upgrade pip

COPY ./requirements.txt /home/app/web

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000
