#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all,delete')

    else:
        name = ""

        @property
        def cities(self):
            """Getter for cities using FileStorage
            """
            city_list = []
            for key, val in models.storage.all(City).items():
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
