#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models import storage_type
from sqlalchemy.orm import relationship
import models
from uuid import uuid4

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel):
    """ A place to stay """
 __tablename__ = 'places'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
	city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
	price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
	amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
	reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

	@property
        def reviews(self):
            """ This returns list of reviews.id """
            d_reviews = models.storage.all('Review').values()
            return [review for review in d_reviews
                    if review.place_id == self.place_id]
	
	@property
        def amenities(self):
         """ This is returning the list of amenity ids """    
	    d_amenities = models.storage.all(Amenity).values()
            return [amenity for amenity in d_amenities
                    if amenity.id in self.amenity_ids]

	@amenities.setter
        def amenities(self, obj):
	    """ This appends the amenity ids to the attribute """
	     if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)

