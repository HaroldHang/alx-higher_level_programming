#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
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
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")