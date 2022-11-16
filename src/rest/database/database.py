from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

connection_str = "postgresql+psycopg2://{}:{}@{}:{}/{}"\
    .format(config("DB_USER"), config("DB_PASSWORD"), config("DB_HOST"), config("DB_PORT"), config("DB_NAME"))
engine = create_engine(connection_str)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
