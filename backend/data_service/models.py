# backend/data_service/models.py

from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date
from typing import Optional


Base = declarative_base()

# Define the table schema
class CustomerQuery(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    subscription_start_date = Column(Date)
    subscription_end_date = Column(Date)
    churned = Column(Boolean, default=False)

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}', email='{self.email}')"


class Customer(BaseModel):
    name: str
    email: str
    subscription_start_date: date
    subscription_end_date: date
    churned: bool = False

    class Config:
        orm_mode = True

class CustomerRead(BaseModel):
    id: int
    name: str
    email: str
    subscription_start_date: Optional[date]
    subscription_end_date: Optional[date]
    churned: bool

    class Config:
        orm_mode = True


class ApiResponse(BaseModel):
    message: str

class Log(BaseModel):
    level: str
    message: str
