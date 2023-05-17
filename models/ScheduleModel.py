from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,Time

Schedules = Table(
    "Schedule",meta,
    Column("id",Integer,primary_key=True),
    Column("schedule_time",Time),
    Column("code",String(45)),
    Column("description",String(255)),
    Column("is_active",Integer)
)