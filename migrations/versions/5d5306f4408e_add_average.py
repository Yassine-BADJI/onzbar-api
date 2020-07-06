"""add_average

Revision ID: 5d5306f4408e
Revises: d32ef5ebb15c
Create Date: 2020-07-06 19:25:03.348889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5306f4408e'
down_revision = 'd32ef5ebb15c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Bars', sa.Column('avg', sa.Float(), nullable=True))
    op.add_column('Drinks', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Drinks', 'price')
    op.drop_column('Bars', 'avg')
    # ### end Alembic commands ###
