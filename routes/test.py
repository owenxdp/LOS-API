from fastapi import APIRouter
from config.db import conn
from models.index import tests
from schemas.index import Test

test = APIRouter()

@test.get('/api/tests')
async def read_data():
    return conn.execute(tests.select()).fetchall()

@test.get('/api/tests/{id}')
async def read_data(id: int):
    return conn.execute(tests.select().where(tests.c.idtest == id)).fetchall()

@test.post('/api/tests')
async def write_data(test : Test):
    conn.execute(tests.insert().values(
        idtest = test.idtest,
        testcol = test.testcol
    ))
    return conn.execute(tests.select()).fetchall()

@test.put('/api/tests/{id}')
async def update_data(id:int, test : Test):
    conn.execute(tests.update().where(tests.c.idtest == id).values(
        idtest = test.idtest,
        testcol = test.testcol
    ))
    return conn.execute(tests.select()).fetchall()

@test.delete('/api/tests')
async def delete_data(id:int):
    conn.execute(tests.delete().where(tests.c.idtest == id))
    return conn.execute(tests.select()).fetchall()