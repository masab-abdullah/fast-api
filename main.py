from fastapi import FastAPI
from routers import user
from database.postgres_connection import test_postgres_connection

app = FastAPI()

# connect router file to main app
app.include_router(user.router)