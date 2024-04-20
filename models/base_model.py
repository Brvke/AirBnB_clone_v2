#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import datetime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

# manage tables
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False,
                unique=True, primary_key=True)
    created_at = Column(
        DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            from models import storage
            try:
                isinstance(kwargs['id'], str)
            except KeyError:
                self.id = str(uuid.uuid4())
            try:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                kwargs['updated_at'] = datetime.now()

            try:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                kwargs['created_at'] = datetime.now()
            
            try:
                del kwargs['__class__']
            except KeyError:
                pass
            self.__dict__.update(kwargs)
        storage.new(self)
        # print(f'new_instance = {self} ')

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        str_dict = self.__dict__.copy() 
        if '_sa_instance_state' in str_dict.keys():
              str_dict.pop('_sa_instance_state')
        return '[{}] ({}) {}'.format(cls, self.id, str_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        """ Delete the curent instanse from storage """
        from models import storage
        storage.delete(self)
