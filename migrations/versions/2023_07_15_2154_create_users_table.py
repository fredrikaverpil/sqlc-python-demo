"""create users table

"""
import sqlalchemy as sa
from alembic import op

from migrations.utils import read_sql

# revision identifiers, used by Alembic.
revision = "310c710c762a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(read_sql(__file__, "upgrade"))


def downgrade() -> None:
    op.execute(read_sql(__file__, "downgrade"))
