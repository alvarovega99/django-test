FROM python:3.8

WORKDIR /app
RUN apt-get update && apt-get install -y netcat

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

COPY /entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
