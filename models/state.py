#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  back_populates="state", cascade="delete")

    def __init__(self, *args, **kwargs):
        """User class init
        """
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """Get a list of all related City objects."""
        city_list = []
        for city in list(models.storage.all(City).values()):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
