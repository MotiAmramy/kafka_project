import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(verbose=True)
engine = create_engine(os.environ['POSTGRESQL_URL'])
session_maker = sessionmaker(bind=engine)



