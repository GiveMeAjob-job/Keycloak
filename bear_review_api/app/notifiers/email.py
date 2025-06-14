from .base import BaseNotifier
import requests

class EmailNotifier(BaseNotifier):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def send(self, user: str, msg: str, meta: dict | None = None) -> None:
        payload = {
            "personalizations": [{"to": [{"email": user}]}],
            "from": {"email": "noreply@example.com"},
            "subject": meta.get("subject") if meta else "Bear Review",
            "content": [{"type": "text/plain", "value": msg}]
        }
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        requests.post("https://api.sendgrid.com/v3/mail/send", json=payload, headers=headers)
