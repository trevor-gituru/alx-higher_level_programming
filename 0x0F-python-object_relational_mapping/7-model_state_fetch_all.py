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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.\
                           format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()

    for id, name in session.query(State.id, State.name).order_by(State.id).all():
        print(f'{id:d}: {name:s}')

    session.close()
