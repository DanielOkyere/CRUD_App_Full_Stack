#!/usr/bin/env python3
"""Validation Schema for User"""

from pydantic import BaseModel
from sqlalchemy import DateTime

class TaskBase(BaseModel):
    name: str

class TaskCreate(TaskBase):
    name: str
    description: str

class TaskSchema(TaskBase):
    date_create : str
    name: str
    description: str
    id: str

    class Config:
        orm_mode = True