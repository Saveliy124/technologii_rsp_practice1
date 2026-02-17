#1.1
from fastapi import FastAPI

application = FastAPI()   

@application.get("/")
async def root():

    return {"message": "Автор елодад действительно работает"}
