"""add foreign key to posts table

Revision ID: cb112aa6b110
Revises: 24eca176f76d
Create Date: 2022-09-14 10:42:34.400146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb112aa6b110'
down_revision = '24eca176f76d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',
                          referent_table='users',local_cols=['owner_id'],
                          remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
