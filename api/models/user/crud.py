#!/usr/bin/env python3
"""CRUD Behavior for User"""

from sqlalchemy.orm import Session
from .users import User
from .schemas import UserCreate
from typing import List
from uuid import uuid4

def get_user_by_phone(db: Session, phone: str):
    """Fetches user by phone number
    Args:
        db: Session Object
        phone: Phone number
    Returns:
        persisted user based on phone number
        """
    return db.query(User).filter(User.phone_number == phone).first()

def create_user(db: Session, user: UserCreate) -> User:
    """Creates a user model and persist to DB
    Args:
        db: Session object
        user: UserCreate object to be validated
    Returns:
        Persisted user model in database
    """
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: str) -> User:
    """Removes persisted User based on Id
    Args:
        db: Session object
        id: String of user id
    Returns:
        User object that was removed
    """
    if isinstance(id, str):
        user = db.query(User).filter(User.id == id).first()
        db.delete(user)
        db.commit()
        return user

def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    """Fetches User from the database paginated
    Args:
        db: Session object
        skip: skip value for pagination
        limit: limit to display
    Returns:
        List of users in the database
    """
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, id: str):
    """Fetches Single user based on id
    Args:
        db: Session Object
        id: String Id for user
    Returns:
        Single user based on Id
    """
    return db.query(User).filter(User.id == id).first()

def update_user(db: Session, arg):
    """Updates User in db"""
    db_user = get_user(db=db, id=arg['id'])
    for k, v in arg:
        if k in db_user:
            setattr(db_user, k, v)
    db.add(db_user)
    db.commit()