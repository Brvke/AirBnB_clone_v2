#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

    if HBNB_TYPE_STORAGE == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False, server_default="NULL")
        places = relationship("Place", cascade="delete")
    else:
        state_id = ""
        name = ""
