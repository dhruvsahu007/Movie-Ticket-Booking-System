from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class MovieCreate(BaseModel):
    title: str
    duration_minutes: int
    genre: str

class showCreate(BaseModel):
    movie_id: int
    screen_id: int
    start_time: date

class BookingCreate(BaseModel):
    user_id: int
    show_id: int
    seat_numbers: List[str]

    
