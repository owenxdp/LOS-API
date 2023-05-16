from fastapi import APIRouter
from config.db import conn
from models.indexModels import Schedules
from schemas.indexSchemas import Schedule

schedule = APIRouter()

@schedule.get('/api/schedule')
async def read_data():
    return conn.execute(Schedules.select()).fetchall()

@schedule.get('/api/schedule/{id}')
async def read_data(id: int):
    return conn.execute(Schedules.select().where(Schedules.c.id == id)).fetchall()

@schedule.post('/api/schedule')
async def write_data(s : Schedule):
    conn.execute(Schedules.insert().values(
        schedule_time = s.schedule_time,
        code = s.code,
        description = s.description
    ))
    return conn.execute(Schedules.select()).fetchall()

@schedule.put('/api/schedule/{id}')
async def update_data(id:int, s : Schedule):
    conn.execute(Schedules.update().where(Schedules.c.id == id).values(
        schedule_time = s.schedule_time,
        code = s.code,
        description = s.description
    ))
    return conn.execute(Schedules.select()).fetchall()

@schedule.delete('/api/schedule')
async def delete_data(id:int):
    conn.execute(Schedules.delete().where(Schedules.c.id == id))
    return conn.execute(Schedules.select()).fetchall()