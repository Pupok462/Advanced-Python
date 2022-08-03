from fastapi import FastAPI
from app_views import router as app_views
from users.api import router as users
from pydantic import constr

app = FastAPI()
app.include_router(app_views)
app.include_router(users)


@app.get("/")
def root():
    return {"message": "Hello World!!!"}


@app.get("/name")
def hello_name(name: constr(min_length=3) = "Vova"):
    """
    GET /name -> Hello , someone
    :param name:
    :return:
    """
    return {"message": f"Hello {name}"}


@app.get("/add")
def add(a: int = 114, b: int = 114):
    return {"message": f"a = {a}, b = {b} , sum = {a + b}"}