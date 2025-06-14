"""initial

Revision ID: 0001_initial
Revises: 
Create Date: 2024-05-01
"""
from alembic import op
import sqlalchemy as sa

revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False, index=True),
        sa.Column('content', sa.Text, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('reviews')
