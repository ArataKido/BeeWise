"""empty message

Revision ID: 837915e21f12
Revises:
Create Date: 2023-10-18 19:48:58.028662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "837915e21f12"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "quizquestionmodel",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("question", sa.String(), nullable=False),
        sa.Column("answer", sa.String(), nullable=False),
        sa.Column(
            "saved_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_quizquestionmodel_id"), "quizquestionmodel", ["id"], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_quizquestionmodel_id"), table_name="quizquestionmodel")
    op.drop_table("quizquestionmodel")
    # ### end Alembic commands ###
