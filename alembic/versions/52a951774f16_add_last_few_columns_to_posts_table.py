"""add last few columns to posts table

Revision ID: 52a951774f16
Revises: cb112aa6b110
Create Date: 2022-09-14 10:47:26.386052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52a951774f16'
down_revision = 'cb112aa6b110'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(),nullable=False, server_default='TRUE'))
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text
        ('NOW()')))
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
