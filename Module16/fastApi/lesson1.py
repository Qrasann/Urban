from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

messages_db = {}

class Message(BaseModel):
  id: int = None
  text: str

@app.get('/')
def get_all_messages(request: Request) -> HTMLResponse:
  return templates.TemplateResponse("message.html", {"request":request, "messages": messages_db})

@app.get("/message/{message_id}")
def get_message(request: Request, message_id: int) -> HTMLResponse:
  try:
    return templates.TemplateResponse("message.html", {"request": request, "messages": message_id})
  except IndexError:
    raise HTTPException(status_code=404, detail='Message not found')

@app.post('/', status_code=status.HTTP_201_CREATED)
def create_message(request: Request, message: str = Form()) -> HTMLResponse:
  if messages_db:
    message_id = max(messages_db, key= lambda m: m.id).id + 1
  else:
    message_id = 0
  messages_db.append(Message(id = message_id, text = message))
  return templates.TemplateResponse('message.html',{"request": request, "messages": messages_db})

@app.put('/message/{message_id}')
def update_message(message_id: int, message: str = Body()) ->str:
  try:
    edit_message = messages_db[message_id]
    edit_message.text = message
    return "Message updated"
  except IndexError:
    raise HTTPException(status_code=404, detail='Message not found')

@app.delete('/message/{message_id}')
def delete_all_message(message_id: int) -> str:
  try:
    messages_db.pop(message_id)
    return f"Message with{message_id} was deleted."
  except IndexError:
    raise HTTPException(status_code=404, detail='Message not found')

@app.delete('/')
def kill_all_messages() -> str:
  messages_db.clear()
  return 'All messages deleted'


"""
@app.post('/')
async def update_message(message_id: str, message: str) -> dict:
  pass

@app.get('/')
async def welcome() -> dict:
  return {'message': 'Hello World'}

@app.get('/user/A/B')
async  def news() -> dict:
  return {'message': f"Hello, Tester!"}

@app.get('/id')
async def id_paginator(username: str = 'Name', age: int = 13) -> dict:
  return {"User": username, "Age": age}

@app.get('/user/{username}/{id}')
async  def news(username: Annotated[str,Path(min_length=3, max_length=15,description='Enter your username', example='montes')]
                , id: int = Path(ge=0,le=100,description="Enter your id", example='75')) -> dict:
  return {'message': f"Hello, {username}: {id}"}"""


