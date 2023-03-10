"""empty message

Revision ID: 10ea2f555c17
Revises: aa7ed2947c85
Create Date: 2022-12-22 14:39:01.201503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10ea2f555c17'
down_revision = 'aa7ed2947c85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
