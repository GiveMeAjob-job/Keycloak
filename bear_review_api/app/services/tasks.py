from celery import Celery

celery_app = Celery('bear_review', broker='redis://redis:6379/0', backend='redis://redis:6379/1')

@celery_app.task
def send_daily_review_reminder(user_id: int) -> str:
    # placeholder implementation
    return f"Reminder sent to {user_id}"
