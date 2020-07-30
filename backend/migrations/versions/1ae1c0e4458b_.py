"""Adds OHLC Table

Revision ID: 1ae1c0e4458b
Revises: 809c8d83b89e
Create Date: 2020-07-24 14:09:39.026721

"""

# revision identifiers, used by Alembic.
revision = '1ae1c0e4458b'
down_revision = '809c8d83b89e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticker_ohlc',
    sa.Column('datetime', sa.DateTime(), nullable=False),
    sa.Column('symbol', sa.String(length=10), nullable=False),
    sa.Column('openz', sa.Float(), nullable=False),
    sa.Column('high', sa.Float(), nullable=False),
    sa.Column('low', sa.Float(), nullable=False),
    sa.Column('close', sa.Float(), nullable=False),
    sa.Column('adj_close', sa.Float(), nullable=False),
    sa.Column('volume', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('datetime', 'symbol')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticker_ohlc')
    # ### end Alembic commands ###
