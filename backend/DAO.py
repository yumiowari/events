from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from mapeamento import *
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class DAO():
    def getSession():
        engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/ticketmaster", echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
