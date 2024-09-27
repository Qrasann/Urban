from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Главная страница"})

@app.get("/user/admin")
async def read_admin():
    return JSONResponse(content={"message": "Вы вошли как администратор"})

@app.get("/user/{user_id}")
async def read_user(
    user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, examples={"default": {"summary": "A typical user ID", "value": 1}})]
):
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"})

@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, examples={"default": {"summary": "A typical username", "value": "UrbanUser"}})],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, examples={"default": {"summary": "A typical age", "value": 24}})]
):
    return JSONResponse(content={"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"})
