FROM python:3.8

WORKDIR /app
RUN apt-get update && apt-get install -y netcat

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

COPY /entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]