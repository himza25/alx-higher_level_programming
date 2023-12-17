#!/usr/bin/python3
"""
Definition of the City class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    The City class:
    - inherits from Base
    - links to the MySQL table cities
    - id: auto-generated, unique integer, primary key
    - name: string of 128 characters, cannot be null
    - state_id: integer, cannot be null, foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
