"""Initial migration

Revision ID: 265e8a36ee5e
Revises: 
Create Date: 2016-01-11 17:13:54.716260

"""

# revision identifiers, used by Alembic.
revision = '265e8a36ee5e'
down_revision = None
branch_labels = None
depends_on = None

import datetime
import websauna.system.model.columns

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activation',
    sa.Column('valid_until', sa.DateTime(), nullable=False),
    sa.Column('created_by', sa.Unicode(length=30), nullable=False),
    sa.Column('code', sa.Unicode(length=30), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    mysql_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('group',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('updated_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('group_data', postgresql.JSONB(), nullable=True),
    sa.Column('description', sa.UnicodeText(), nullable=True),
    sa.Column('name', sa.Unicode(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    mysql_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('users',
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('salt', sa.String(length=256), nullable=True),
    sa.Column('created_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('updated_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('activated_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.Column('last_login_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('last_login_ip', postgresql.INET(), nullable=True),
    sa.Column('user_data', postgresql.JSONB(), nullable=True),
    sa.Column('last_auth_sensitive_operation_at', websauna.system.model.columns.UTCDateTime(), nullable=True),
    sa.Column('registered_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('activation_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('security_code', sa.Unicode(length=256), nullable=True),
    sa.Column('email', sa.Unicode(length=100), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['activation_id'], ['activation.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('security_code'),
    sa.UniqueConstraint('username'),
    mysql_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('usergroup',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8',
    mysql_engine='InnoDB'
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usergroup')
    op.drop_table('users')
    op.drop_table('group')
    op.drop_table('activation')
    ### end Alembic commands ###
