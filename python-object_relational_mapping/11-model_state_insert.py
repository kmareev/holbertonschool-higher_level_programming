#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    connect_str = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"

    engine = create_engine(connect_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
