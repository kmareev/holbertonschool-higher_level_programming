#!/usr/bin/python3
"""A python file that contains a class definition of a
City an instance base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


Base = declarative_base()

class City(Base):
    """Representing the base class of City in a database"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
