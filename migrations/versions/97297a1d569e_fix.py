"""Fix.

Revision ID: 97297a1d569e
Revises: 4cf33c00e5e7
Create Date: 2021-04-26 18:19:05.879846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97297a1d569e'
down_revision = '4cf33c00e5e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('announcement', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'announcement')
    # ### end Alembic commands ###
