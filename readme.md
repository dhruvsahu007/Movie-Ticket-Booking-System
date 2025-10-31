well documented readme file

# Movie Ticket Booking System
This is a simple movie ticket booking system built with FastAPI. It allows users to view movies, book tickets, and manage their bookings. Admin users can add theaters, movies, and screens.
## Features
- User registration and authentication
- View available movies and showtimes
- Book and cancel tickets
- Admin panel for managing theaters, movies, and screens
## Technologies Used
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
## Installation
1. Clone the repository:
   ```bash
   git clone
    cd movie-ticket-system
    ```
2. Create a virtual environment and activate it:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


    ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
    python create_db.py
    ```
5. Run the application:

    ```bash
     uvicorn main:app --reload
     ```
6. Open your browser and navigate to `http://
    localhost:8000/docs` to access the API documentation.
## Usage
- Register a new user or log in with existing credentials.  
- Browse available movies and showtimes.
- Book tickets for your desired movie and showtime.
- Admin users can log in to access the admin panel and manage theaters, movies, and screens.
