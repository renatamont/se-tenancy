# STANDARD PART IMPORTS
import logging

# THIRD PART IMPORTS
import psycopg2 as pg
from decouple import config
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, text


class PostgresDBInfrastructure:

    @classmethod
    def get_postgres_connection(cls):
        try:
            connection = pg.connect(
                host=config("HOST_POSTGRES"),
                port=config("PORT_POSTGRES"),
                database=config("DATABASE_POSTGRES"),
                user=config("USER_POSTGRES"),
                password=config("PASSWORD_POSTGRES")
            )

            logging.info("Successfully Connected to Postgres")

            return connection

        except (Exception, pg.Error) as error:
            print("Error when connecting with Postgres", error)

    @classmethod
    def get_session(cls, schema: str):
        connection = PostgresDBInfrastructure.get_postgres_connection()
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
        Session = scoped_session(sessionmaker(bind=engine))
        session = Session()

        # Set the search path to the specified schema
        session.execute(text(f'SET search_path TO {schema}'))

        return session
