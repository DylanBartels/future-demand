"""create events table

Revision ID: 4d3b8682be61
Revises: 
Create Date: 2022-02-17 19:09:34.363718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4d3b8682be61"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "event",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("date", sa.Date()),
        sa.Column("time", sa.Time()),
        sa.Column("location", sa.String()),
        sa.Column("title", sa.String()),
        sa.Column("artists", sa.ARRAY(sa.String)),
        sa.Column("works", sa.ARRAY(sa.String)),
        sa.Column("image_link", sa.String),
    )


def downgrade():
    op.drop_table("event")
