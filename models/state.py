#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class
    Attributes:
        __tablename__(str): states table in MySQLdb
        name(String): states' name
        cities(): relationship between cities and states table
    """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize state"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Lists all related cit objects
            """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
