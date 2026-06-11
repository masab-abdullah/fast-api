from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome Abdullah"}

from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "About Page"}

@app.get("/student")
def student():
    return {
        "name": "Abdullah",
        "age": 18
    }
@app.get("/info")
def api_info():
    return {
        "name": "My First FastAPI Project",
        "version": "1.0",
        "description": "This API is created for learning FastAPI basics",
        "author": "Abdullah",
        "status": "running"
    }