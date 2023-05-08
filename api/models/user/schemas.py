#!/usr/bin/env python3
"""Validation Schema for User"""

from pydantic import BaseModel

class UserBase(BaseModel):
    phone_number: str

class UserCreate(UserBase):
    first_name: str
    last_name: str

class UserSchema(UserBase):
    first_name: str
    last_name: str
    id: str

    class Config:
        orm_mode = True