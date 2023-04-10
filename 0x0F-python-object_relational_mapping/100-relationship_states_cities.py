#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]
    myEngine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pas, db), pool_pre_ping=True)
    Base.metadata.create_all(myEngine)

    Session = sessionmaker(bind=myEngine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()