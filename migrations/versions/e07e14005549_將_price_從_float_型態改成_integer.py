"""將 price 從 float 型態改成 integer

Revision ID: e07e14005549
Revises: ebd93f10a1de
Create Date: 2023-06-06 09:32:09.094288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e07e14005549'
down_revision = 'ebd93f10a1de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column(
            'price', existing_type=sa.FLOAT(), type_=sa.Integer(), existing_nullable=True
        )
        batch_op.alter_column(
            'current_price', existing_type=sa.FLOAT(), type_=sa.Integer(), existing_nullable=True
        )

    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column(
            'price', existing_type=sa.FLOAT(), type_=sa.Integer(), existing_nullable=True
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('record', schema=None) as batch_op:
        batch_op.alter_column(
            'price', existing_type=sa.Integer(), type_=sa.FLOAT(), existing_nullable=True
        )

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column(
            'current_price', existing_type=sa.Integer(), type_=sa.FLOAT(), existing_nullable=True
        )
        batch_op.alter_column(
            'price', existing_type=sa.Integer(), type_=sa.FLOAT(), existing_nullable=True
        )

    # ### end Alembic commands ###
