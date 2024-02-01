FROM python:3.11

WORKDIR /app
COPY . .

RUN apt-get update && pip install -r requirements.txt

EXPOSE 5000
CMD [ "python3","main.py" ]