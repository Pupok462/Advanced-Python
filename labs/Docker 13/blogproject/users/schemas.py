from pydantic import BaseModel, constr, Field
from uuid import uuid4


class UserBase(BaseModel):
    username: constr(min_length=8) = Field(..., example="Johnathan")


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=123)


def make_token():
    token = str(uuid4())
    print("New token", token)
    return token


class User(UserOut):
    token: str = Field(default_factory=make_token)

