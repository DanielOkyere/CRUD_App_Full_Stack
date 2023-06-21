from fastapi import APIRouter, Depends, HTTPException
from models.tasks import schemas, crud
from sqlalchemy.orm import Session
from dependencies.db_dependency import get_db

router = APIRouter(
    prefix="/tasks", tags=["tasks"],
    responses={404: {"description": "Not Found"}}
)


@router.post("/", response_model=schemas.TaskSchema)
def create_user(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.get_task_by_name(db, phone=task.name)
    if db_task:
        raise HTTPException(status_code=400, detail="Task Already Exist")
    return crud.create_task(db=db, task=task)


@router.get("/", response_model=list[schemas.TaskSchema])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}", response_model=schemas.TaskSchema)
def read_user(task_id: str, db: Session = Depends(get_db)):
    db_tasks = crud.get_task(db, id=task_id)
    if db_tasks is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_tasks

@router.delete("/{task_id}")
def delete_tasks(user_id: str, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id=user_id)


@router.put("/{task_id}", response_model=schemas.TaskSchema)
def update_tasks(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    try:
        updated_task = crud.update_task(db, task)
        return updated_task
    except:
        raise HTTPException(status_code=404, detail="Update Failed")
    
    
