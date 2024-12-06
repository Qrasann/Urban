from fastapi import FastAPI
from models.task import router as task_router
from models.user import router as user_router
from backend.db import Base, engine

# Создание таблиц в БД
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to TaskManager"}

app.include_router(task_router)
app.include_router(user_router)
