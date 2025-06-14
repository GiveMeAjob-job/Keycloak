from .base import BaseNotifier
import requests

class PushNotifier(BaseNotifier):
    def send(self, user: str, msg: str, meta: dict | None = None) -> None:
        data = {
            "to": user,
            "sound": "default",
            "title": meta.get("title") if meta else "Bear Review",
            "body": msg,
        }
        requests.post("https://exp.host/--/api/v2/push/send", json=data)
