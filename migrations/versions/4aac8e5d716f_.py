"""empty message

Revision ID: 4aac8e5d716f
Revises: d1c4298e4a92
Create Date: 2022-11-04 12:03:42.959324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aac8e5d716f'
down_revision = 'd1c4298e4a92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False, auto_increment=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('author')
    # ### end Alembic commands ###
