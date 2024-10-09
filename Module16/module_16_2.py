from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            ge=1, le=100,
            examples={"example": 1}
        )
    ]
):
    return {"user_id": user_id}

@app.get("/user/{username}/{age}")
async def get_user_with_age(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            min_length=5, max_length=20,
            examples={"example": "UrbanUser"}
        )
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            ge=18, le=120,
            examples={"example": 24}
        )
    ]
):
    return {"username": username, "age": age}
