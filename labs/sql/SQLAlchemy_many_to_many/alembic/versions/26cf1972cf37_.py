"""empty message

Revision ID: 26cf1972cf37
Revises: 
Create Date: 2022-07-29 20:38:18.542221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "26cf1972cf37"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("username", sa.String(length=20), nullable=True),
        sa.Column(
            "priority", sa.Boolean(), server_default="FALSE", nullable=True
        ),
        sa.Column("e_mail", sa.String(length=70), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=20), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("books", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=20), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["authors.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("posts")
    op.drop_table("authors")
    op.drop_table("users")
    # ### end Alembic commands ###
