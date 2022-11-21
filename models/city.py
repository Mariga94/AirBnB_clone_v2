#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name

    Attributes:
        __tablename__(str): cities table in MySQLdb
        state_id(String): the state id
        name(String): the state name
    """
    __tablename__ = 'cities'
    __table_args__ = (
            {'mysql_default_charset': 'latin1'})
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place",
                          backref="cities",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

