from fastapi import, APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import admin_required
from app import models

router = APIRouter()

@router.post("/theaters/", dependencies=[Depends(admin_required)])
def create_theater(name: str, location: str, db: Session = Depends(get_db)):
    db_theater = models.Theater(name=name, location=location)
    db.add(db_theater)
    db.commit()
    db.refresh(db_theater)
    return db_theater
@router.post("/movies/", dependencies=[Depends(admin_required)])
def create_movie(title: str, description: str, duration_minutes: int, theater_id: int, db: Session = Depends(get_db)):
    db_movie = models.Movie(
        title=title,
        description=description,
        duration_minutes=duration_minutes,
        theater_id=theater_id,
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
@router.post("/screens/", dependencies=[Depends(admin_required)])
def create_screen(theater_id: int, name: str, seating_capacity: int, db
: Session = Depends(get_db)):
    db_screen = models.Screen(
        theater_id=theater_id, name=name, seating_capacity=seating_capacity
    )
    db.add(db_screen)
    db.commit()
    db.refresh(db_screen)
    return db_screen

