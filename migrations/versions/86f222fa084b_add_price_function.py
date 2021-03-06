"""add_price_function

Revision ID: 86f222fa084b
Revises: d32ef5ebb15c
Create Date: 2020-07-06 20:35:09.898826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f222fa084b'
down_revision = 'd32ef5ebb15c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Bars', sa.Column('avg', sa.Float(), nullable=True))
    op.add_column('Bars', sa.Column('happyhour', sa.String(length=50), nullable=True))
    op.add_column('Bars', sa.Column('openhour', sa.String(length=50), nullable=True))
    op.add_column('Drinks', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('Drinks', sa.Column('price_happyhour', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Drinks', 'price_happyhour')
    op.drop_column('Drinks', 'price')
    op.drop_column('Bars', 'openhour')
    op.drop_column('Bars', 'happyhour')
    op.drop_column('Bars', 'avg')
    # ### end Alembic commands ###
