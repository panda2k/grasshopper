"""empty message

Revision ID: c8c00cc2f9ed
Revises: a6ae96bacbe0
Create Date: 2024-04-20 11:25:55.188827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'c8c00cc2f9ed'
down_revision: Union[str, None] = 'a6ae96bacbe0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authenticationsession', sa.Column('credential', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authenticationsession', 'credential')
    # ### end Alembic commands ###
