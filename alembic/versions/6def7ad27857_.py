"""empty message

Revision ID: 6def7ad27857
Revises: c8c00cc2f9ed
Create Date: 2024-04-20 13:22:16.690338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '6def7ad27857'
down_revision: Union[str, None] = 'c8c00cc2f9ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('location', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('event', sa.Column('time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'time')
    op.drop_column('event', 'location')
    # ### end Alembic commands ###
