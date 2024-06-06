# backend/api_service/endpoints/customer.py

from datetime import date
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import Boolean, Column, Integer, MetaData, String, Date, Table, select
from sqlalchemy.orm import Session
from backend.config.logging import logger
from backend.data_service import models as data_models
from backend.data_service.database import Base, SessionLocal, engine
from backend.data_service.models import  CustomerRead, ApiResponse, CustomerQuery, Customer


router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@router.post("/create_customer/", response_model=ApiResponse)
async def create_customer(customer_data: Customer, db: Session = Depends(get_db)):
    # Create a new customer
    try:
        customer_initial = CustomerQuery(**customer_data.dict())
        db.add(customer_initial)

        db.commit()
        logger.info("Customer created successfully.")
        return {"message": "Customer created successfully."}
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating customer: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/read_customer/{customer_id}", response_model=CustomerRead)
async def read_customer(customer_id: int, db: Session = Depends(get_db)):
    try:
        customer = db.query(Customer).filter(Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        return customer
    except Exception as e:
        logger.error(f"Error reading customer: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/update_customer/{customer_id}", response_model=ApiResponse)
async def update_customer(customer_id: int, customer_data: Customer, db: Session = Depends(get_db)):
    # Update customer details
    try:
        customer = db.query(data_models.Customer).filter(data_models.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        for key, value in customer_data.dict().items():
            setattr(customer, key, value)
        db.commit()
        logger.info("Customer updated successfully.")
        return {"message": "Customer updated successfully."}
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating customer: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/delete_customer/{customer_id}", response_model=ApiResponse)
async def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    # Delete customer
    try:
        customer = db.query(data_models.Customer).filter(data_models.Customer.id == customer_id).first()
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        db.delete(customer)
        db.commit()
        logger.info("Customer deleted successfully.")
        return {"message": "Customer deleted successfully."}
    except Exception as e:
        db.rollback()
        logger.error(f"Error deleting customer: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/view_customers/", response_model=List[CustomerRead])
async def view_customers (db: Session = Depends(get_db)):
    # View all customers in the database
    try:
        customer_instances = db.query(CustomerQuery).all()
        customers = [CustomerRead.from_orm(customer) for customer in customer_instances]
        return customers
    except Exception as e:
        logger.error(f"Error viewing database: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/add_customers_in_bulk/", response_model=ApiResponse)
async def add_customers_in_bulk(customers: List[Customer], db: Session = Depends(get_db)):
    # Add customers in bulk
    try:
        customer_objects = [data_models.CustomerQuery(**customer.dict()) for customer in customers]
        db.add_all(customer_objects)
        db.commit()
        logger.info(f"{len(customers)} customers added in bulk.")
        return {"message": f"{len(customers)} customers added in bulk."}
    except Exception as e:
        db.rollback()
        logger.error(f"Error adding customers in bulk: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")