class ApiError(Exception):
    pass

class ApiTimeoutError(ApiError):
    pass

class ApiResponseError(ApiError):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(message)