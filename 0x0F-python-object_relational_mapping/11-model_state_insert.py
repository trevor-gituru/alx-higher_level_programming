#!/usr/bin/python3
"""
adding the state lous
parameters: username, password, database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    mysql_db = {
        'drivername': 'mysql',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3],
        'host': 'localhost',
        'port': 3306
    }
    engine = create_engine(URL.create(**mysql_db))
    Session = sessionmaker(bind=engine)
    session = Session()

    lous = State(name='Louisiana')
    session.add(lous)
    session.commit()
    print(lous.id)

    session.close()
