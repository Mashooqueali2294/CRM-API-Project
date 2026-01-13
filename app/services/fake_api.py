from app.core.http_client import AsyncHTTPClient
from app.model.users import User

client = AsyncHTTPClient("https://jsonplaceholder.typicode.com")

async def get_users():
    data = await client.request("GET", "/users")
    return [User(**user) for user in data]

async def create_post(data: dict):
    return await client.request("POST", "/posts", json=data)