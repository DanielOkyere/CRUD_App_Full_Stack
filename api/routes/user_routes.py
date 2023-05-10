from fastapi import APIRouter, Depends, HTTPException
from models.user import schemas, crud
from sqlalchemy.orm import Session
from dependencies.db_dependency import get_db

router = APIRouter(
    prefix="/users", tags=["users"],
    responses={404: {"description": "Not Found"}}
)


@router.post("/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_phone(db, phone=user.phone_number)
    if db_user:
        raise HTTPException(status_code=400, detail="Phone Number already exist")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[schemas.UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=schemas.UserSchema)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id=user_id)
