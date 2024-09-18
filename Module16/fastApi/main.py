from fastapi import FastAPI
from fastapi.responses import  JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
  return JSONResponse(content={"message": 'Главная страница'})

@app.get('/user/admin')
async def read_admin():
  return JSONResponse(content={'message':'Вы вошли как администратор'})

@app.get('/user/{user_id}')
async def read_user(user_id: int):
  return JSONResponse(content={'message': f"Вы вошли как пользователь №:{user_id}"})

@app.get('/user')
async def read_user_info(username: str, age: int):
  return JSONResponse(content={'message':f"Информация о пользователе. Имя: {username}, Возраст: {age}"})