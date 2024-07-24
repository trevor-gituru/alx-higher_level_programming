#!/usr/bin/python3
"""
all City objects
parameters: username, password, database name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import relationship
from sqlalchemy.engine.url import URL


if __name__ == "__main__":
    mysql_db = {
        'drivername': 'mysql',
        'username': argv[1],
        'password': argv[2],
        'database': argv[3],
        'host': 'localhost',
    }
    engine = create_engine(URL.create(**mysql_db))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    State.cities = relationship(City, order_by=City.id, back_populates='state')

    for city in session.query(City).order_by(City.id).all():
        print(f"{city.state.name:s}: ({city.id:d}) {city.name:s}")
    session.commit()
    session.close()
