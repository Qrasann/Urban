# app/main.py
from app.db import engine, Base
from fastapi import FastAPI

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
