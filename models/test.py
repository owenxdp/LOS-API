from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


tests=Table(
    'test',meta,
    Column("idtest",Integer,primary_key=True),
    Column("testcol",String(45)),
)