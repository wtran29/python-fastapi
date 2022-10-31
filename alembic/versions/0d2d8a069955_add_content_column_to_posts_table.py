"""add content column to posts table

Revision ID: 0d2d8a069955
Revises: e1685b2412bc
Create Date: 2022-10-30 11:14:42.702816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d2d8a069955'
down_revision = 'e1685b2412bc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
