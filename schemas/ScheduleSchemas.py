from pydantic import BaseModel

class Schedule(BaseModel):
    schedule_time:str
    code:str
    description:str
    is_active:int
