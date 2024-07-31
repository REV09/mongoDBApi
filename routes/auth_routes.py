from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from models.User_class import User
from config.jwt_functions import write_token, validate_token


auth_routes = APIRouter()


@auth_routes.post('/login')
def login(user: User):
    if user.username == 'admin':
        return write_token(dict(user))
    else:
        return JSONResponse(content={"message": "Username not found"}, status_code=404)


@auth_routes.post('/verify/token')
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(' ')[1]
    return validate_token(token, output=True)
