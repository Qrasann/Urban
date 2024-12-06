from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from backend.db_depends import get_db
from backend.db import Base
from sqlalchemy import Column, Integer, String
from schemas import CreateUser, UpdateUser
from slugify import slugify
from typing import Annotated


# Модель базы данных
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    slug = Column(String, nullable=False)

# APIRouter для маршрутов
router = APIRouter()

@router.post("/user/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status_code": 201, "transaction": "Successful"}

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Функция обновления пользователя
@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, updated_data: UpdateUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    slug = slugify(updated_data.firstname + updated_data.lastname)  # Используем имя и фамилию для slug
    user.firstname = updated_data.firstname
    user.lastname = updated_data.lastname
    user.age = updated_data.age
    user.slug = slug

    db.commit()
    db.refresh(user)
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}

# Функция удаления пользователя
@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

    db.delete(user)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User deletion is successful!"}
