#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    pas = sys.argv[2]
    db = sys.argv[3]
    myEngine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pas, db))
    Base.metadata.create_all(myEngine)
    Session = sessionmaker(bind=myEngine)
    session = Session()
    for instance in session.query(State).filter(State.name.like('%a%')):
        session.delete(instance)
    session.commit()
