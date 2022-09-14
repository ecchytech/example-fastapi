"""add content column to posts table

Revision ID: 10a1e893b210
Revises: d064ff489287
Create Date: 2022-09-14 10:31:01.772674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10a1e893b210'
down_revision = 'd064ff489287'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
