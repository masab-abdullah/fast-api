from fastapi import FastAPI
from routers import user

app = FastAPI()

# connect router file to main app
app.include_router(user.router)