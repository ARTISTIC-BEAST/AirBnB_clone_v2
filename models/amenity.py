#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity
from models import storage_type


class Amenity(BaseModel):
 '''This is the amenity class'''
    if models.storage_t == 'db':
      	__tablename__ = 'amenities'
       	name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializing the Amenity"""
        super().__init__(*args, **kwargs)

