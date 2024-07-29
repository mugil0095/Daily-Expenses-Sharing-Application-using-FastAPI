from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext
from app.schemas import UserCreate
from app.models import User

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
print("Passlib imported and CryptContext created successfully.")

def create_user(db, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        email=user.email,
        name=user.name,
        mobile_number=user.mobile_number,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(description=expense.description, amount=expense.amount, payer_id=expense.payer_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    for split in expense.splits:
        db_split = models.ExpenseSplit(
            expense_id=db_expense.id,
            user_id=split.user_id,
            amount=split.amount,
            percentage=split.percentage,
            split_type=split.split_type
        )
        db.add(db_split)
    
    db.commit()
    return db_expense

def get_user_expenses(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.payer_id == user_id).all()

def get_all_expenses(db: Session):
    return db.query(models.Expense).all()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)