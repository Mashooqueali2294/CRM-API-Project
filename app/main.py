import asyncio
from app.services.fake_api import get_users, create_post

async def main():
    users = await get_users()
    print(f"Fetched {len(users)} users")

    post = await create_post({
        "title": "Async Test",
        "body": "Production ready client",
        "userId": 1
    })

    print("Post Created:", post)


if __name__ == "__main__":
    asyncio.run(main())