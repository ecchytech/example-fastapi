"""add user table

Revision ID: 24eca176f76d
Revises: 10a1e893b210
Create Date: 2022-09-14 10:35:29.919053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24eca176f76d'
down_revision = '10a1e893b210'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                        server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
