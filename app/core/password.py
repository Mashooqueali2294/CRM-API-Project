from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()

def hashed_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)