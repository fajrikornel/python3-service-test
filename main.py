from config import config
from server.server import app

app_port = config.settings.app_port

app.run(host="0.0.0.0", port=app_port)
