from fastapi import FastAPI
from routes.index import test
app = FastAPI()

app.include_router(test)