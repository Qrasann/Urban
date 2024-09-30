from fastapi import APIRouter

task_router = APIRouter(prefix='/task', tags=['task'])

@task_router.get('/')
def all_tasks():
    pass

@task_router.get('/{task_id}')
def task_by_id(task_id: int):
    pass

@task_router.post('/create')
def create_task():
    pass

@task_router.put('/update')
def update_task():
    pass

@task_router.delete('/delete')
def delete_task():
    pass
