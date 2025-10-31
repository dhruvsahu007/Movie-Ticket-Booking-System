from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app import models

router = APIRouter()

@router.get("/movies/")
def list_movies(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    movies = db.query(models.Movie).all()
    return movies   
@router.post("/bookings/")
def create_booking(show_id: int, seat_ids: list[int], db: Session = Depends
                     (get_db), current_user: str = Depends(get_current_user)):
     user = db.query(models.User).filter(models.User.username == current_user).first()
     if not user:
          return {"error": "User not found"}
    
     db_booking = models.Booking(user_id=user.id, show_id=show_id)
     db.add(db_booking)
     db.commit()
     db.refresh(db_booking)
    
     for seat_id in seat_ids:
          db_seat_booking = models.SeatBooking(booking_id=db_booking.id, seat_id=seat_id)
          db.add(db_seat_booking)
    
     db.commit()
     return db_booking  

@router.get("/bookings/")
def list_bookings(db: Session = Depends(get_db), current_user: str = Depends(get
_current_user)):
    user = db.query(models.User).filter(models.User.username == current_user).first()
    if not user:
        return {"error": "User not found"}
    bookings = db.query(models.Booking).filter(models.Booking.user_id == user.id).all()
    return bookings
