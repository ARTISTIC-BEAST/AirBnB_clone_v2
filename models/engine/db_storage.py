#!/usr/bin/python3
""" the database storage engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


class DBStorage:
    """ seting up the db storage engine """
    __engine = None
    __session = None
    classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


    def __init__(self):
        """ instantiating the new dbstorage instance"""
        HBNB_user = getenv('HBNB_MYSQL_USER')
        HBNB_pwd = getenv('HBNB_MYSQL_PWD')
        HBNB_host = getenv('HBNB_MYSQL_HOST')
        HBNB_db = getenv('HBNB_MYSQL_DB')
        HBNB_env = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           HBNB_user, HBNB_pwd,
                                           HBNB_host, HBNB_db
                                       ), pool_pre_ping=True)

        if HBNB_env == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """query on the current db session for all cls objects"""
        my_dct = {}
        if cls is None:
            for cl in classes.values():
                objs_list = self.__session.query(cl).all()
                for obj in objs_list:
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dct[key] = obj
        else:
            objs_list = self.__session.query(cls).all()
            for obj in objs_list:
                key = obj.__class__.__name__ + '.' + obj.id
                my_dct[key] = obj
        return my_dct

    def new(self, obj):
        """adding the obj to the current db session"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """ saving a new record (object) to table """
        self.__session.commit()

    def delete(self, obj=None):
        """ deleting object (record) from table """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload engine """
        try:
            Base.metadata.create_all(self.__engine)
        except Exception:
            pass
        R_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(R_session)
        self.__session = Session()


    def close(self):
        """ closing the session"""
        self.__session.close()
