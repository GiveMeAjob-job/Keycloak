class BaseNotifier:
    def send(self, user: str, msg: str, meta: dict | None = None) -> None:
        raise NotImplementedError
