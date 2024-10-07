from fastapi import FastAPI
from app.task import router as task_router
from app.user import router as user_router

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task_router)
app.include_router(user_router)
