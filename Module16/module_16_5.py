from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates  # Импортируем только Jinja2Templates
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()

# Настраиваем папку с шаблонами
templates = Jinja2Templates(directory="templates")

# Список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Получение всех пользователей и отображение их в шаблоне
@app.get("/", response_class=HTMLResponse)
async def get_all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# Получение информации о конкретном пользователе
@app.get("/users/{user_id}", response_class=HTMLResponse)
async def get_user_by_id(request: Request, user_id: int = Path(..., title="The ID of the user to get")):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

# Создание нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    new_id = 1 if not users else users[-1].id + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user

# Обновление данных пользователя
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Удаление пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User not found")