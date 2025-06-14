from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

class Review(BaseModel):
    id: int | None = None
    user_id: int
    content: str

router = APIRouter(prefix="/reviews", tags=["reviews"])

FAKE_DB: dict[int, Review] = {}

@router.get("/", response_model=List[Review])
def list_reviews() -> List[Review]:
    return list(FAKE_DB.values())

@router.post("/", response_model=Review, status_code=201)
def create_review(review: Review) -> Review:
    review.id = len(FAKE_DB) + 1
    FAKE_DB[review.id] = review
    return review

@router.put("/{review_id}", response_model=Review)
def update_review(review_id: int, review: Review) -> Review:
    if review_id not in FAKE_DB:
        raise HTTPException(status_code=404, detail="Not found")
    review.id = review_id
    FAKE_DB[review_id] = review
    return review

@router.delete("/{review_id}", status_code=204)
def delete_review(review_id: int) -> None:
    if review_id in FAKE_DB:
        del FAKE_DB[review_id]
    return None
