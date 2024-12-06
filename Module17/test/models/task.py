from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import task
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

router = APIRouter(prefix="/task", tags=["task"])



@router.get("/tasks")
def get_tasks():
    return {"message": "Task management routes are active!"}

# Получить все задачи
@router.get("/")
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

# Получить задачу по ID
@router.get("/{task_id}")
def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task was not found")

# Создать новую задачу
@router.post("/create")
def create_task(task: CreateTask, db: Annotated[Session, Depends(get_db)]):
    stmt = insert(Task).values(
        title=task.title,
        content=task.content,
        priority=task.priority
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Task creation is successful!"}

# Обновить задачу по ID
@router.put("/update/{task_id}")
def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    stmt = update(Task).where(Task.id == task_id).values(
        title=task.title,
        content=task.content,
        priority=task.priority
    )
    result = db.execute(stmt)
    db.commit()
    if result.rowcount:
        return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}
    raise HTTPException(status_code=404, detail="Task was not found")

# Удалить задачу по ID
@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = delete(Task).where(Task.id == task_id)
    result = db.execute(stmt)
    db.commit()
    if result.rowcount:
        return {"status_code": status.HTTP_200_OK, "transaction": "Task deletion is successful!"}
    raise HTTPException(status_code=404, detail="Task was not found")
