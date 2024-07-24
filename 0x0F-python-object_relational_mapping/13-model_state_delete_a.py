#!/usr/bin/python3
"""
deleting states with names containing a
parameters: username, password, database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sys import argv
from model_state import Base, State

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

    # Delete state object
    session.query(State).filter(State.name.like('%a%')).delete()
    
    session.commit()

    session.close
