FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "chess_engines.wsgi:application"]