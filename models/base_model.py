#!/usr/bin/python3
"""
Base model for the Airbnb console
"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """
    The base class of the project
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    if self.created_at or self.updated_at:
                        value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Update the updated_at instance with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return dict representation of the instance
        """
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict

    def __str__(self):
        """
        String representation of the object
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, str(self.id), self.__dict__)
