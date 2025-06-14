from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from unified_auth import require_user

class Review(BaseModel):
    id: int | None = None
    user_id: int
    content: str

router = APIRouter(prefix="/reviews", tags=["reviews"])

FAKE_DB: dict[int, Review] = {}

@router.get("/", response_model=List[Review], dependencies=[Depends(require_user)])
def list_reviews(user=Depends(require_user)) -> List[Review]:
    return list(FAKE_DB.values())

@router.post("/", response_model=Review, status_code=201, dependencies=[Depends(require_user)])
def create_review(review: Review, user=Depends(require_user)) -> Review:
    review.id = len(FAKE_DB) + 1
    FAKE_DB[review.id] = review
    return review

@router.put("/{review_id}", response_model=Review, dependencies=[Depends(require_user)])
def update_review(review_id: int, review: Review, user=Depends(require_user)) -> Review:
    if review_id not in FAKE_DB:
        raise HTTPException(status_code=404, detail="Not found")
    review.id = review_id
    FAKE_DB[review_id] = review
    return review

@router.delete("/{review_id}", status_code=204, dependencies=[Depends(require_user)])
def delete_review(review_id: int, user=Depends(require_user)) -> None:
    if review_id in FAKE_DB:
        del FAKE_DB[review_id]
    return None
