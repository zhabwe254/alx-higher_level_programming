#!/usr/bin/python3
"""Module to define the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """City class linked to cities table"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
