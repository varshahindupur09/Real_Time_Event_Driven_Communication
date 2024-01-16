"""Initial migration

Revision ID: c2052f8c6199
Revises: 
Create Date: 2024-11-11 19:26:10.870579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2052f8c6199'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_product_user_id'), 'product_user', ['id'], unique=False)
    op.create_unique_constraint('user_product_unique', 'product_user', ['user_id', 'product_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_product_unique', 'product_user', type_='unique')
    op.drop_index(op.f('ix_product_user_id'), table_name='product_user')
    # ### end Alembic commands ###