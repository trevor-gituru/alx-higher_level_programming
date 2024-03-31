#!/usr/bin/python3
"""
lists all State objects from database hbtn_0e_6_usa
parameters: username, password, database name
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
                           @localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
