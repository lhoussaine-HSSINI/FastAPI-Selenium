from fastapi import FastAPI, BackgroundTasks, HTTPException
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

    


