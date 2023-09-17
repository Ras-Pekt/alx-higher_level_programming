#!/usr/bin/python3
"""
contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class State(Base):
#     """mapping class for table states"""
#     __tablename__ = "states"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(128), nullable=False)

class City(Base):
    """mapping class for table cities"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
