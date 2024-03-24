#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    This represents the base of all other classes in the aBnb project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel class.

        Args:
            args(any): unused
            kwargs(dict): key/value pairs of attributes.
        """

        tformt = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        # retrive the current local time and date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # convert string object into ISO format
        if len(kwargs) != 0:
            for k, p in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(p, tformt)
                else:
                    self.__dict__[k] = p
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns the dictornary representation of the BaseModel.

        include key/value pairs of __class__ representing
        the class name of the object.
        """
        pdict = self.__dict__.copy()
        pdict["created_at"] = self.created_at.isoformat()
        pdict["updated_at"] = self.updated_at.isoformat()
        pdict["__class__"] = self.__class__.__name__
        return pdict

    def __str__(self):
        """
        Return a string representation of a BaseModel instance.
        """
        cls_name = self.__class__.__name__

        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
