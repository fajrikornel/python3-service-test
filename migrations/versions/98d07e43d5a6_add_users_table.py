"""add users table

Revision ID: 98d07e43d5a6
Revises: 
Create Date: 2023-11-22 16:44:19.546616

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, BIGINT, TEXT, TIMESTAMP


# revision identifiers, used by Alembic.
revision: str = '98d07e43d5a6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        Column("id", BIGINT(), primary_key=True),
        Column("name", TEXT(), nullable=False),
        Column("passkey", TEXT(), nullable=False),
        Column("created_at", TIMESTAMP(), nullable=False),
        Column("updated_at", TIMESTAMP(), nullable=False)
    )


def downgrade() -> None:
    pass
