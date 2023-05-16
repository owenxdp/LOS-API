from fastapi import FastAPI
from routes.indexRoutes import schedule
app = FastAPI()

app.include_router(schedule)