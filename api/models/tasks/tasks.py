#!/usr/bin/env python3
""" User Class """

from db.database import Base
from sqlalchemy import Column, Integer, String

class Task(Base):
    """
    Class: User
        Inherits from declarative Base
        and creates user model
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    date_created = Column(String)
