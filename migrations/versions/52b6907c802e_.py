"""empty message

Revision ID: 52b6907c802e
Revises: 
Create Date: 2024-05-07 23:46:33.887879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52b6907c802e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('api_key', sa.String(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_key'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
