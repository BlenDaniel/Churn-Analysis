# backend/api_service/endpoints/dataset.py

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.config.logging import logger
from backend.data_service import models as data_models
from backend.data_service.database import SessionLocal
from backend.data_service.models import Customer, Customer, ApiResponse


router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/load/", response_model=ApiResponse)
async def loadJson(customer_data: List[Customer], db: Session = Depends(get_db)):
    try:
        for customer in customer_data:
            customer_entry = data_models.Customer(**customer.dict())
            db.add(customer_entry)
        
        db.commit()
        logger.info("Customers loaded and stored successfully.")
        return {"message": "Customers loaded and stored successfully."}
    except Exception as e:
        db.rollback()
        logger.error(f"Error loading customers: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
