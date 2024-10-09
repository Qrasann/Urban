from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=1,
            max_length=100
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=1,
            le=120
        )
    ]
):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        str,
        Path(
            title="Enter user ID",
            min_length=1
        )
    ],
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=1,
            max_length=100
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=1,
            le=120
        )
    ]
):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return f"User {user_id} not found"

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[
        str,
        Path(
            title="Enter user ID",
            min_length=1
        )
    ]
):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"
