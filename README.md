# Future-demand

## Description
* Use Python to write a script to crawl events (date, time, location, title, artists, works and image link) from in the following link: https://www.lucernefestival.ch/en/program/summer-festival-22
* Create an endpoint that lists all the events happening (title and date)
* Insert data into database (PostgreSQL) - propose a schema that makes sense for the use case
* dockerize your solution so we can run it with docker compose

## Quickstart

```
docker-compose up
```

visit: http://0.0.0.0:3000/docs#/

Be sure scrapper is done 

## Preparation

- Try to keep it simple (KISS principle)
- Facilitate possibility for fast adoptation of scraper when html changes
- Be fancy and try out psycopg3 and sqlmodel

## Steps

1. Explore website to gain insight for datamodel
2. Create datamodel
3. write scraper
- Download hmtl for local testing
- Write scraper functions
- Rewrite to class due to shared state
4. write backend
- fastapi
- alembic
5. make datamodel shared
6. write full docker-compose

## Schema

EVENT

| Column           | Datatype      | Info
|------------------|---------------|------------------
| id (pk)          | int           |
| date             | date          |
| time             | time          | (HH:MM:SS)
| location         | string        | 
| title            | string        |
| artists          | array(string) |
| work             | array(string) | artist - song (with separator ("-"))

Could make two different tables for artists and works, due to higher cardinality. But that seems a litle much for the usecase, so decided to do one table.

## In case of html change

Will probably be detected by the [scraper](./src/scraper.py) and raise an exception on line 47. User can troubleshoot diff with the test [html-file](./tests/data/main.html) and come up with a new ccs selectors. The new css selectors can be given as environmental variables to a already deployed scraper.

For next change replace the testing htmlfile and overwrite the environmental variable default of the scrapper.

## Tests

```
python -m unittest tests/test_scraper.py
```

## Encoutered problems

Wanted to use the latest and greatest psycopg3 in combination with sqlmodel but this is not possible untill sqlalchemy [releases 2.0](https://github.com/sqlalchemy/sqlalchemy/issues/6842). so went back to psycopg2.