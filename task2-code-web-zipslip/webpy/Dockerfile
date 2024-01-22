FROM python:3.11

RUN addgroup phughj && adduser phughj --disabled-password --ingroup phughj

WORKDIR /app
RUN chown -R phughj:phughj /app

COPY --chown=phughj:phughj ./requirements.txt ./requirements.txt

RUN apt-get update && \
    apt-get install -y unzip

USER phughj
RUN pip3 install --user -r requirements.txt

COPY --chown=phughj:phughj . .

EXPOSE 5000

CMD [ "python3", "main.py" ]
