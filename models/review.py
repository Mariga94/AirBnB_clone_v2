#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    __table_args__ = (
            {'mysql_default_charset': 'latin1'})

    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)
