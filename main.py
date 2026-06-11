
from fastapi import FastAPI
from fastapi import users 

app = FastAPI()

app.include_router(users.router) 