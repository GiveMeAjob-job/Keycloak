# Bear Review Backend

This service provides CRUD endpoints for managing reviews along with a celery task queue for notifications.

## Database
Tables are managed via Alembic. The initial revision creates a `reviews` table with fields `id`, `user_id`, and `content`.

## Endpoints
- `GET /reviews` list reviews
- `POST /reviews` create a new review
- `PUT /reviews/{id}` update a review
- `DELETE /reviews/{id}` delete a review

## Celery
A basic task `send_daily_review_reminder` is defined in `app/services/tasks.py`.
