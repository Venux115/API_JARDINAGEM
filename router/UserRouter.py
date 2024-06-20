from fastapi import APIRouter, Request
from controller.UserController import UserController

router_user = APIRouter()
users = UserController()

@router_user.get("/user/")
def home():
    return "aoba"

@router_user.get("/user/{id}")
def get_user(id: int):
    return users.get(id)

@router_user.post("/user/")
def add_user(user_data: dict):
    return users.add(user_data)