"""Add newProp column

Revision ID: acae3f9d6b28
Revises: e138a68372e2
Create Date: 2025-01-11 16:15:58.955297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acae3f9d6b28'
down_revision: Union[str, None] = 'e138a68372e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_account', sa.Column('newProp', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_account', 'newProp')
    # ### end Alembic commands ###
