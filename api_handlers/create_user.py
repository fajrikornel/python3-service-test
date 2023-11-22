from models.users import User
import models.users as users


def create_user(name: str, passkey: str):
    print(f"Creating user with name {name}")
    user = User()
    user.name = name
    user.passkey = passkey

    users.create(user)
    print(f"Done creating user with name {name}")
