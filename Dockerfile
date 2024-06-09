FROM python:3.10-slim-buster


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY src /app
WORKDIR /app

COPY src .

EXPOSE 3000/tcp

CMD ["python3", "-m", "aiohttp.web", "-H", "0.0.0.0", "-P", "3000", "app:create_app"]