#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from models import storage_type


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """ getting attributes that returns City instances"""
	    d_cities = models.storage.all(City)
            return [city for city in d_cities.values()
                    if city.state_id == self.id]
