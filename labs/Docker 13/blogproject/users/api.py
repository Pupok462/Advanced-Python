from . import crud
from .schemas import UserIn, UserOut, User
from fastapi import APIRouter, HTTPException, Depends
from starlette.status import HTTP_404_NOT_FOUND
from .dependencies import get_user_by_auth_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserOut])
def list_users():
    return crud.list_users()


@router.post("", response_model=UserOut)
def create_user(user_in: UserIn):
    return crud.create_user(user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_auth_token)):
    return user


@router.get("/{user_id}", response_model=UserOut, responses={HTTP_404_NOT_FOUND: {"description": "user not found"}})
def get_user_id(user_id: int):
    user = crud.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail=F"User with id : {user_id} - not found")
