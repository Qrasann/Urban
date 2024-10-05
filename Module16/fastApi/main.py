from fastapi import FastAPI, Path
from pydantic import BaseModel, constr, conint
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
    user_id: Annotated[conint(ge=1, le=100), Path(description='Enter User ID')]
):
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"})

@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[constr(min_length=5, max_length=20), Path(description='Enter username')],
    age: Annotated[conint(ge=18, le=120), Path(description='Enter age')]
):
    return JSONResponse(content={"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"})
