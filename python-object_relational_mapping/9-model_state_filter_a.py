#!/usr/bin/python3
"""Lists all State objects that contain the
letter 'a' from the database hbtn_0e_6_usa
"""
# Import necessary modules and functions
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

# Create a connection string w/ username, pw and db name
# Establish a connection to db
    connect_str = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"


# Create a session to interact with db
    engine = create_engine(connect_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

# Query the state objects with letter 'a'
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
