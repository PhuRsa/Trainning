FROM php:8.2-apache

WORKDIR /var/www/html/
COPY ./src .

RUN chown -R root:www-data /var/www/html
RUN chmod 750 /var/www/html
RUN sh clearNote.sh