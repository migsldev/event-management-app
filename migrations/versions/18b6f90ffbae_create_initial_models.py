"""Create Initial models

Revision ID: 18b6f90ffbae
Revises: dfc76e5534e4
Create Date: 2024-08-06 12:50:11.443444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18b6f90ffbae'
down_revision: Union[str, None] = 'dfc76e5534e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###