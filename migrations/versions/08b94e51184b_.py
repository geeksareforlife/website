"""

Revision ID: 08b94e51184b
Revises: 2ad5fa906742
Create Date: 2016-07-16 16:25:36.622581

"""

# revision identifiers, used by Alembic.
revision = '08b94e51184b'
down_revision = '2ad5fa906742'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.create_unique_constraint('_venue_name_type_uniq', ['name', 'type'])

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.drop_constraint('_venue_name_type_uniq', type_='unique')

    ### end Alembic commands ###