#!/usr/bin/python3
"""Module for the class BaseModel"""
from uuid import uuid4
from datetime import datetime
from copy import deepcopy


class BaseModel:
    """The basemodel class"""
    form = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self):
        """Constructor of the class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = deepcopy(self.created_at)

    def save(self):
        """Will save objects"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation"""
        dct = {}

        dct.update(self.__dict__)
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = self.created_at.strftime(BaseModel.form)
        dct["updated_at"] = self.updated_at.strftime(BaseModel.form)

        return dct

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
