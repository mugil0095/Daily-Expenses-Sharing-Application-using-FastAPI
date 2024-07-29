from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Enum, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base
import enum

Base = declarative_base()

class SplitTypeEnum(str, enum.Enum):
    equal = "equal"
    exact = "exact"
    percentage = "percentage"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    mobile_number = Column(String)
    hashed_password = Column(String)

    # Relationships
    expenses = relationship("Expense", back_populates="payer")
    splits = relationship("ExpenseSplit", back_populates="user")

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Integer)
    payer_id = Column(Integer, ForeignKey('users.id'))

    payer = relationship("User", back_populates="expenses")
    splits = relationship("ExpenseSplit", back_populates="expense")

class ExpenseSplit(Base):
    __tablename__ = 'expense_splits'

    id = Column(Integer, primary_key=True, index=True)
    expense_id = Column(Integer, ForeignKey('expenses.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Integer)
    percentage = Column(Integer)
    split_type = Column(String)

    expense = relationship("Expense", back_populates="splits")
    user = relationship("User", back_populates="splits")

User.expenses = relationship("Expense", back_populates="payer")
Expense.splits = relationship("ExpenseSplit", back_populates="expense")

# Define the engine
engine = create_engine('mysql+pymysql://Mugil:Mugil3004@localhost/expense_sharing')

# Create all tables
Base.metadata.create_all(engine)