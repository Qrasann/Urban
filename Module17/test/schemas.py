from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

    class Config:
        from_attributes = True  # Замените orm_mode на from_attributes


# Модель для создания пользователя, slug не передается пользователем
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

# Модель для обновления пользователя, slug не обновляется
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

# Модели для задачи

# Модель для создания задачи
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

# Модель для обновления задачи
class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
