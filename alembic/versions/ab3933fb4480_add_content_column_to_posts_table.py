"""add content column to posts table

Revision ID: ab3933fb4480
Revises: 769f90ce4923
Create Date: 2025-06-22 00:51:25.786410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab3933fb4480'
down_revision: Union[str, Sequence[str], None] = '769f90ce4923'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
