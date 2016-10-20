"""empty message

Revision ID: 124d9fa0e807
Revises: caa6fd9f09c1
Create Date: 2016-10-20 14:54:02.025313

"""

# revision identifiers, used by Alembic.
revision = '124d9fa0e807'
down_revision = 'caa6fd9f09c1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('list', sa.Column('slug', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_list_slug'), 'list', ['slug'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_list_slug'), table_name='list')
    op.drop_column('list', 'slug')
    ### end Alembic commands ###
