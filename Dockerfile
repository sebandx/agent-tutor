FROM python:3.13-slim 

WORKDIR /app

RUN apt-get update && apt-get install -y racket && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

EXPOSE 8080

CMD ["poetry", "run", "adk", "web", "--host=0.0.0.0", "--port=8080"]
