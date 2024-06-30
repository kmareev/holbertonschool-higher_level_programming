#!/usr/bin/python3
"""Prints all cities from the database hbtn_0e_14_usa"""

#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    connect_str = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"

    engine = create_engine(connect_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State, City).join(city).order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) ({city.name}")

    session.close()
