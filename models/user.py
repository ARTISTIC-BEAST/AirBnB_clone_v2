#!/usr/bin/python3
"""This module defines a User class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """Defines User"""
    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all,delete")
        reviews = relationship("Review", backref="user", cascade="all,delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
