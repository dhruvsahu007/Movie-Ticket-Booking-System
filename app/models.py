from sqlalchemy import column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = column(Integer, primary_key=True, index=True)
    username = column(String, unique=True, index=True, nullable=False)
    email = column(String, unique=True, index=True, nullable=False)
    hashed_password = column(String, nullable=False)
    is_admin = column(Integer, default=0)

    bookings = relationship("Booking", back_populates="user")

class Theater(Base):
    __tablename__ = "theaters"

    id = column(Integer, primary_key=True, index=True)
    name = column(String, unique=True, index=True, nullable=False)
    location = column(String, nullable=False)

    movies = relationship("Movie", back_populates="theater")

class Screen(Base):
    __tablename__ = "screens"

    id = column(Integer, primary_key=True, index=True)
    theater_id = column(Integer, ForeignKey("theaters.id"), nullable=False)
    name = column(String, nullable=False)
    seating_capacity = column(Integer, nullable=False)

    theater = relationship("Theater", back_populates="screens")
    shows = relationship("Show", back_populates="screen")

class Seat(Base):
    __tablename__ = "seats"

    id = column(Integer, primary_key=True, index=True)
    screen_id = column(Integer, ForeignKey("screens.id"), nullable=False)
    seat_number = column(String, nullable=False)
    seat_type = column(String, nullable=False)  # e.g., Regular, VIP

    screen = relationship("Screen", back_populates="seats") 

class Movie(Base):
    __tablename__ = "movies"

    id = column(Integer, primary_key=True, index=True)
    title = column(String, nullable=False)
    description = column(String)
    duration_minutes = column(Integer, nullable=False)
    theater_id = column(Integer, ForeignKey("theaters.id"), nullable=False)

    theater = relationship("Theater", back_populates="movies")
    shows = relationship("Show", back_populates="movie")

class Show(Base):
    __tablename__ = "shows"

    id = column(Integer, primary_key=True, index=True)
    movie_id = column(Integer, ForeignKey("movies.id"), nullable=False)
    screen_id = column(Integer, ForeignKey("screens.id"), nullable=False)
    start_time = column(DateTime, nullable=False)
    end_time = column(DateTime, nullable=False)

    movie = relationship("Movie", back_populates="shows")
    screen = relationship("Screen", back_populates="shows")
    bookings = relationship("Booking", back_populates="show")

class Booking(Base):
    __tablename__ = "bookings"

    id = column(Integer, primary_key=True, index=True)
    user_id = column(Integer, ForeignKey("users.id"), nullable=False)
    show_id = column(Integer, ForeignKey("shows.id"), nullable=False)
    booking_time = column(DateTime, default=datetime.datetime.utcnow)
    total_amount = column(Float, nullable=False)

    user = relationship("User", back_populates="bookings")
    show = relationship("Show", back_populates="bookings")
    booked_seats = relationship("BookedSeat", back_populates="booking")

