#!/usr/bin/env python3
"""CRUD Behavior for User"""

from sqlalchemy.orm import Session
from .tasks import Task
from .schemas import TaskCreate
from typing import List
from uuid import uuid4

def get_task_by_name(db: Session, name: str):
    """Fetches task by name
    Args:
        db: Session Object
        name: task name
    Returns:
        persisted task
        """
    return db.query(Task).filter(Task.name == name).first()

def create_task(db: Session, task: TaskCreate) -> Task:
    """Creates a task model and persist to DB
    Args:
        db: Session object
        task: UserCreate object to be validated
    Returns:
        Persisted user model in database
    """
    db_task = Task(
        name=task.name,
        description=task.description,
        date_created=task.dat
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, id: str) -> Task:
    """Removes persisted User based on Id
    Args:
        db: Session object
        id: String of user id
    Returns:
        User object that was removed
    """
    if isinstance(id, str):
        task = db.query(Task).filter(Task.id == id).first()
        db.delete(task)
        db.commit()
        return task

def get_tasks(db: Session, skip: int = 0, limit: int = 10) -> List[Task]:
    """Fetches task from the database paginated
    Args:
        db: Session object
        skip: skip value for pagination
        limit: limit to display
    Returns:
        List of tasks in the database
    """
    return db.query(Task).offset(skip).limit(limit).all()

def get_task(db: Session, id: str):
    """Fetches Single task based on id
    Args:
        db: Session Object
        id: String Id for task
    Returns:
        Single task based on Id
    """
    return db.query(Task).filter(Task.id == id).first()

def update_task(db: Session, arg):
    """Updates User in db"""
    db_user = get_task(db=db, task=arg['id'])
    for k, v in arg:
        if k in db_user:
            setattr(db_user, k, v)
    db.add(db_user)
    db.commit()