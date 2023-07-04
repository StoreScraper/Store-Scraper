from fastapi import FastAPI
from models import User

db = []
app = FastAPI()

@app.post("/user/")
async def user(user: User):
    db


@app.get("/")
def root():
    return {"message": "Hello Store Scrapper"}