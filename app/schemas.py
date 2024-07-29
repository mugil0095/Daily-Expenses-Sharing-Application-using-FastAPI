from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from enum import Enum

class UserBase(BaseModel):
    email: EmailStr
    name: str
    mobile_number: str

class UserCreate(BaseModel):
    email: str
    name: str
    mobile_number: str
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class SplitTypeEnum(str, Enum):
    equal = "equal"
    exact = "exact"
    percentage = "percentage"

class ExpenseBase(BaseModel):
    description: str
    amount: float
    payer_id: int

class ExpenseCreate(ExpenseBase):
    splits: List['ExpenseSplitCreate']

class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True

class ExpenseSplitBase(BaseModel):
    expense_id: int
    user_id: int
    amount: Optional[float] = None
    percentage: Optional[float] = None
    split_type: SplitTypeEnum

class ExpenseSplitCreate(ExpenseSplitBase):
    pass

class ExpenseSplit(ExpenseSplitBase):
    id: int

    class Config:
        orm_mode = True
