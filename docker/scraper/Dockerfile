FROM python:3.10.0-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

COPY ./requirements-scraper.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./src ./

CMD python scraper.py