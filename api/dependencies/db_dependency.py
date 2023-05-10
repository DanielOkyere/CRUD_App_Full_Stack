#!/usr/bin/env python3
"""Handle Db Sessions"""

from db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()