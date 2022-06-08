"""new users-table

Revision ID: 270d62503112
Revises: ffdc0a98111c
Create Date: 2022-06-07 19:35:56.723945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '270d62503112'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('full_name', sa.String(length=55), nullable=False))
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'admin')
    op.drop_column('users', 'full_name')
    # ### end Alembic commands ###
