from app.services.fake_api import get_users, create_post

if __name__ == "__main__":
    users = get_users()
    print(f"Fetched {len(users)} users")
    

    post = create_post({
        "title": "Test",
        "body": "Retry + logging working",
        "userId": 1
    })

    print("Post Created:", post)