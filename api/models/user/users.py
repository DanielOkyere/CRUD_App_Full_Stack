#!/usr/bin/env python3
""" User Class """

from api.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class User(Base):
    """
    Class: User
        Inherits from declarative Base
        and creates user model
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    phone_number = Column(String, unique=True, index=True)
