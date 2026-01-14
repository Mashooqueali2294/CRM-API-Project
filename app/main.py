from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token

app = FastAPI()

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin" or form_data.password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": form_data.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }