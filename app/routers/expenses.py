from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)

@router.get("/users/{user_id}/expenses/", response_model=List[schemas.Expense])
def read_user_expenses(user_id: int, db: Session = Depends(get_db)):
    expenses = crud.get_user_expenses(db, user_id=user_id)
    if expenses is None:
        raise HTTPException(status_code=404, detail="No expenses found for this user")
    return expenses

@router.get("/expenses/", response_model=List[schemas.Expense])
def read_all_expenses(db: Session = Depends(get_db)):
    return crud.get_all_expenses(db)
