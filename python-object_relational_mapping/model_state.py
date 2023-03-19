#!/usr/bin/python3
""" task 6 """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """ creating a table """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
