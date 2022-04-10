#!/usr/bin/python3
"""define the state class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class state"""


    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)
