#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import models


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(128))
    number_rooms = Column(Integer(0), nullable=False)
    number_bathrooms = Column(Integer(0), nullable=False)
    max_guest = Column(Integer(0), nullable=False)
    price_by_night = Column(Integer(0), nullable=False)
    latitude = Column(Float())
    longitude = Column(Float())
    amenity_ids = []
    if models.storage_t == 'db':
        reviews = relationship("Review",  back_populates="place", cascade="delete")
    else:
        @property
        def reviews(self):
            """Get a list of all reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
