from flask import Flask, request
from config import config
import api_handlers.create_user as create_user_handler

app_name = config.settings.app_name

app = Flask(app_name)


@app.route("/users/create", methods=["POST"])
def create_user():
    headers = request.headers

    name = headers.get("x-name")
    passkey = headers.get("x-passkey")

    print(f"Received create user request with name {name}")
    if name is None or passkey is None:
        return {"success": False}

    create_user_handler.create_user(name, passkey)

    return {"success": True}
