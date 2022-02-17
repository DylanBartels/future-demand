FROM python:3.10.0-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

COPY ./requirements-api.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install uvicorn==0.17.5

COPY ./src /

RUN chmod +x /bin/startup.sh

CMD exec ./bin/startup.sh