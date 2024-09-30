from fastapi import APIRouter

user_router = APIRouter(prefix='/user', tags=['user'])

@user_router.get('/')
def all_users():
    pass

@user_router.get('/{user_id}')
def user_by_id(user_id: int):
    pass

@user_router.post('/create')
def create_user():
    pass

@user_router.put('/update')
def update_user():
    pass

@user_router.delete('/delete')
def delete_user():
    pass
