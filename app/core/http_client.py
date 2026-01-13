import requests
from app.core.retry import retry_request
from app.core.logger import logger
from app.config.settings import Settings

class HttpClient:
    def __init__(self, base_url: str, headers: dict | None = None):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}

    @retry_request
    def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"{method.upper()} {url}")


        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            timeout=Settings.API_TIMEOUT,
            **kwargs
        )

        if response.status_code >= 400:
            raise Exception(
                f"HTTP {response.status_code}: {response.text}"
            )

        return response.json()
