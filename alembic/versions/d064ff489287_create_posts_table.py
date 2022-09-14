"""create posts table

Revision ID: d064ff489287
Revises: 
Create Date: 2022-09-14 10:19:49.139024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd064ff489287'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id',sa.Integer(),nullable=False, primary_key=True),
    sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
