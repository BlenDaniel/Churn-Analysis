# backend/data_service/models.py

from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    email: str
    subscription_start_date: str
    subscription_end_date: str
    churned: bool = False

class Log(BaseModel):
    level: str
    message: str

class ApiResponse(BaseModel):
    message: str
