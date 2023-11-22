FROM python:3.9.6-buster

COPY /.env.sample /app/.env
COPY . /app
WORKDIR /app
RUN pip install poetry
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "main.py"]
