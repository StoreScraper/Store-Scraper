from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    id: int
    user_name = str
    email = str
    password = str
    joined = date