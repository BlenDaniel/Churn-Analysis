# backend/data_service/models.py

from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    subscription_start_date = Column(Date)
    subscription_end_date = Column(Date)
    churned = Column(Boolean, default=False)

class CustomerCreate(BaseModel):
    name: str
    email: str
    subscription_start_date: date
    subscription_end_date: date
    churned: bool = False

class ApiResponse(BaseModel):
    message: str

class Log(BaseModel):
    level: str
    message: str
