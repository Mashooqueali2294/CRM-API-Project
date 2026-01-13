from app.core.http_client import HttpClient

client = HttpClient("https://jsonplaceholder.typicode.com")

def get_users():
    return client.request("GET", "/users")

def create_post(data: dict):
    return client.request("POST", "/posts", json=data)