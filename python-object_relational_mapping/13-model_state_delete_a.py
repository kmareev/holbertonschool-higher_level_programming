#!/usr/bin/python3
"""Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
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

    delete_state = session.query(State).filter(State.name.like('%a%')).all()

    for state in delete_state:
        session.delete(state)
    session.commit()

    session.close()
