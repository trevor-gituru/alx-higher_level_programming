#!/usr/bin/python3
"""
printing the first state object from database hbtn_0e_6_usa
parameters: username, password, database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')

    session.close()
