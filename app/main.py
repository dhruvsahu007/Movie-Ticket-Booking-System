from fastapi import FastAPI
from app import auth, admin_routes, user_routes
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin_routes.router)
app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Ticket Booking System API"}