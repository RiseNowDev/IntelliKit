"""Reorganize

Revision ID: b7e412330dfa
Revises: 7073dd457477
Create Date: 2024-08-06 10:34:59.223284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7e412330dfa'
down_revision: Union[str, None] = '7073dd457477'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('validation_rules',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('field_name', sa.String(), nullable=False),
    sa.Column('rule_type', sa.Enum('REGEX', 'MIN_LENGTH', 'MAX_LENGTH', 'REQUIRED', 'EMAIL', 'TAX_ID', 'VAT', 'COUNTRY_CODE', name='ruletype'), nullable=False),
    sa.Column('rule_value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('validation_rules')
    # ### end Alembic commands ###
