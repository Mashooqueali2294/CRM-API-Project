import httpx
from app.core.retry import async_retry_request
from app.core.logger import logger
from app.core.exceptions import ApiTimeoutError, ApiResponseError
from app.config.settings import Settings

class AsyncHTTPClient:
    def __init__(self, base_url: str, headers: dict | None = None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}

    @async_retry_request
    async def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip("/")}"
        logger.info(f"{method.upper()} {url}")

        try:
            async with httpx.AsyncClient(timeout=Settings.API_TIMEOUT) as client:
                response = await client.request(
                    method,
                    url,
                    headers=self.headers,
                    **kwargs
                )
        except httpx.TimeoutException:
            raise ApiTimeoutError("API request time out")
        if response.status_code >= 400:
            raise ApiResponseError(
                response.status_code,
                response.text
            )
        
        try:
            return response.json()
        except ValueError:
            raise ApiResponseError(
                response.status_code,
                "Invalid JSON response"
            )