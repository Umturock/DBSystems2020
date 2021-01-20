import psycopg2
from decouple import config

DB_URL = config("DATABASE_URL")
Schema = [open("schema.sql", "r").read()]


if __name__ == '__main__':
    with psycopg2.connect(DB_URL) as connection:
        with connection.cursor() as cur:
            for statement in Schema:
                cur.execute(statement)
                connection.commit()
