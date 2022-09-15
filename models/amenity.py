#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models.base_model import Base
import models

if models.storage_t == 'db':
    from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity  class
    Attributes:
        name (str): Amenity  name
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if models.storage_t == 'db':
        place_amenities = relationship("Place", secondary=place_amenity,
                                       backref='amenities')

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
