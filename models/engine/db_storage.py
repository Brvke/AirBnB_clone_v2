#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBstorage:
    """This class manages the storage of hbnb model in MySql"""
    __engine = None
    __session = None
    HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
    HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
    HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
    HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
    HBNB_ENV = os.getenv('HBNB_ENV')
    classes = [City, State, User]

    def __init__(self):
        """Instanciates a new DBstorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(DBstorage.HBNB_MYSQL_USER,
                                                 DBstorage.HBNB_MYSQL_PWD,
                                                 DBstorage.HBNB_MYSQL_HOST,
                                                 DBstorage.HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if DBstorage.HBNB_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Instance that querys a database session"""

        # searches for all values of an instance of an obj or all objects
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """creates a new instance of obj"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session if obj is not none"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reloads all objs"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ call remove() method on the private
            session attribute (self.__session) """
        self.__session.close()
