from datetime import datetime, timedelta
from jose import jwt, JWSError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth_scheme)):
    try:
        payload = jwt.decode(token, "SUPER_SECRET_KEY", algorithms=["HS256"])
        return payload["sub"]
    except JWSError:
        raise HTTPException(status_code=401, detail="Invalid token")