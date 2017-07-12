"""empty message

Revision ID: d178731b1b5f
Revises: 32de948690fa
Create Date: 2017-07-01 14:41:55.470162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd178731b1b5f'
down_revision = '32de948690fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=70), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
