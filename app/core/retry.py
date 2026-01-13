import time
from app.config.settings import Settings
from app.core.logger import logger

def retry_request(func):
    def wrapper(*args, **kwargs):
        for attempt in range(1, Settings.MAX_RETRIES + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.warning(f"Attempt {attempt} failed: {e}")
                if attempt == Settings.MAX_RETRIES:
                    raise
                time.sleep(Settings.RETRY_BACKOFF * attempt)
    return wrapper