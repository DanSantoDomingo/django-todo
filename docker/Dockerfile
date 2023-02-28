FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry && poetry config virtualenvs.create false
RUN poetry install --without dev --no-root

COPY . /code/
RUN chmod +x docker/entrypoint.sh
RUN chmod +x docker/start_django.sh

ENTRYPOINT ["/code/docker/entrypoint.sh"]
