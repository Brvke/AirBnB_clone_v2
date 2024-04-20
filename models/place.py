#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, INTEGER, FLOAT
from sqlalchemy.orm import relationship


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column("place_id", String(60), ForeignKey(
        'places.id'),  nullable=False),
    Column("amenity_id", String(60), ForeignKey(
        'amenities.id'),  nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    __tablename__ = 'places'
    if HBNB_TYPE_STORAGE == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False, server_default="NULL")
        description = Column(String(1024), nullable=True, server_default="NULL")
        number_rooms = Column(INTEGER, default=0, nullable=False)
        number_bathrooms = Column(INTEGER, default=0, nullable=False)
        max_guest = Column(INTEGER, default=0, nullable=False)
        price_by_night = Column(INTEGER, default=0, nullable=False)
        latitude = Column(FLOAT, default=0, nullable=False)
        longitude = Column(FLOAT, default=0, nullable=False)
        reviews = relationship("Review", cascade="delete", backref="places")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)

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
        store = FileStorage()

        @property
        def cities(self):
            """Getter attribute for cities class"""
            place_list = []
            for key, value in Place.store.all().items():
                if value['__class__'] == 'City':
                    if value.place_id == self.id:
                        place_list.append(value)
            return place_list

        @property
        def reviews(self):
            """Getter attribute for cities class"""
            review_list = []
            for key, value in Place.store.all().items():
                if value['__class__'] == 'Review':
                    if value.id == self.id:
                        review_list.append(value)
            return review_list
