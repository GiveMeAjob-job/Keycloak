from fastapi import FastAPI
from .routers import reviews

app = FastAPI(title="Bear Review API", version="1.0.0-alpha")

app.include_router(reviews.router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
