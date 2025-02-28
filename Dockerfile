FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc libc-dev libffi-dev libssl-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x /app/engines/stockfish_13/stockfish && \
    chmod +x /app/engines/komodo_12/komodo

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "chess_engines.wsgi:application"]