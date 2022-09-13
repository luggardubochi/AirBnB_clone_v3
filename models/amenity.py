#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity  class
    Attributes:
        name (str): Amenity  name
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)