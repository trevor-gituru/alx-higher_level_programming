#!/usr/bin/python3
"""
state object with name passed as argument
parameters: username, password, database name, searched state
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
    
    searched_state = argv[4]

    engine = create_engine(URL.create(**mysql_db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=searched_state).first()
    if state:
        print(state.id)
    else:
        print('Not found')

    session.close()
