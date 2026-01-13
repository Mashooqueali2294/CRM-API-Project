import asyncio
from app.config.settings import Settings
from app.core.logger import logger


def async_retry_request(func):
    async def wrapper(*args, **kwargs):
        for attempt in range(1, Settings.MAX_RETRIES + 1):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.warning(f"Attempt {attempt} failed: {e}")
                if attempt == Settings.MAX_RETRIES:
                    raise
                await asyncio.sleep(Settings.RETRY_BACKOFF * attempt)
    return wrapper