"""add_drinks_table

Revision ID: d32ef5ebb15c
Revises: f25776c2c76f
Create Date: 2020-07-06 12:02:03.438799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd32ef5ebb15c'
down_revision = 'f25776c2c76f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Drinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bar_id'], ['Bars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Drinks')
    # ### end Alembic commands ###
