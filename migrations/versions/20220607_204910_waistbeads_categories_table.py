"""waistbeads-categories table

Revision ID: bfdf5d212519
Revises: 4d997402aa75
Create Date: 2022-06-07 20:49:10.127997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfdf5d212519'
down_revision = '4d997402aa75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('waistbeads_categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('waistbead_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['waistbead_id'], ['waistbeads.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'waistbead_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('waistbeads_categories')
    # ### end Alembic commands ###
