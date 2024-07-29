# app/main.py

from fastapi import FastAPI
from app.routers import users, expenses
from app.database import engine, Base
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])

# Create database tables
@app.on_event("startup")
async def on_startup():
    try:
        # Create the tables in the database
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except SQLAlchemyError as e:
        print(f"Error creating database tables: {e}")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API!"}
