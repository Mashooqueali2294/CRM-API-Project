import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", 5))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))
    RETRY_BACKOFF = float(os.getenv("RETRY_BACKOFF", 0.5))

    DATABASE_URL= os.getenv("DATABASE_URL")
    JWT_SECRET_KEY= os.getenv("JWT_SECRET_KEY")
    JWT_EXPIRE_MINUTES= os.getenv("JWT_EXPIRE_MINUTES")
