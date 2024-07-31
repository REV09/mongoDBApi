from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
import os
from fastapi.responses import JSONResponse


def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days=days)
    return new_date


def write_token(data: dict):
    api_key: str = os.getenv('SECRET')
    token = encode(payload={**data, "exp": expire_date(1)}, key=api_key, algorithm="HS256")
    return token


def validate_token(token, output=False):
    api_key: str = os.getenv('SECRET')
    try:
        if output:
            return decode(token, key=api_key, algorithms=["HS256"])
        decode(token, key=api_key, algorithms=["HS256"])

    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Token is invalid."}, status_code=401)

    except exceptions.ExpiredSignature:
        return JSONResponse(content={"message": "Token is expired."}, status_code=401)
