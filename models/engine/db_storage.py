#!/usr/bin/python3
"""
Script that creates a new engine to communicate with database
"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


# All enviroment varibles
env = {
    "USER": os.environ.get('HBNB_MYSQL_USER'),
    "PWD": os.environ.get('HBNB_MYSQL_PWD'),
    "HOST": os.environ.get('HBNB_MYSQL_HOST'),
    "DB": os.environ.get('HBNB_MYSQL_DB'),
    "STORAGE": os.environ.get('HBNB_TYPE_STORAGE'),
    "ENV": os.environ.get('HBNB_ENV')
}


class DBStorage:
    """New engine class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for instance of this class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(env['USER'],
                                              env['PWD'],
                                              env['HOST'],
                                              env['DB']),
                                      pool_pre_ping=True)
        if env['ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to query all objects depending of the class"""

        classes = ['User', 'Place', 'State', 'City', 'Amenity', 'Review']
        dictionary = {}

        if cls is None:
            for _class in classes:
                result = self.__session.query(eval(_class)).all()
                for obj in result:
                    dictionary[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            result = self.__session.query(eval('cls')).all()
            for obj in result:
                dictionary[obj.__class__.__name__ + '.' + obj.id] = obj
        return dictionary

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close and remove session connection to database"""
        self.__session.remove()
