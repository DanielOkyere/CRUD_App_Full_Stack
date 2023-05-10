#!/usr/bin/env python3
""" Init File For CRUD API"""

from fastapi import FastAPI, Depends, Request
from db.database import engine, Base
from routes import user_routes
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*']
)

app.include_router(user_routes.router)


@app.get('/')
async def home():
    return {"message": "API is Alive"}
