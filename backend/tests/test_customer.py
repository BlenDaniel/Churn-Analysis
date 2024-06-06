import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.data_service.models import Customer, CustomerCreate
from backend.data_service.database import get_db

def test_create_customer(client: TestClient, test_db):
    response = client.post(
        "/customer/create_customer/",
        json={"name": "John Doe", "email": "john.doe@example.com",
              "subscription_start_date": "2022-01-01", "subscription_end_date": "2023-01-01"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Customer created successfully."}

def test_get_customer(client: TestClient, test_db):
    response = client.post(
        "/customer/create_customer/",
        json={"name": "Jane Doe", "email": "jane.doe@example.com",
              "subscription_start_date": "2022-01-01", "subscription_end_date": "2023-01-01"}
    )
    assert response.status_code == 200
    response = client.get("/customer/get_customer/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"

def test_update_customer(client: TestClient, test_db):
    response = client.put(
        "/customer/update_customer/1",
        json={"name": "John Smith", "email": "john.smith@example.com",
              "subscription_start_date": "2022-01-01", "subscription_end_date": "2023-01-01"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Customer updated successfully."}
    response = client.get("/customer/get_customer/1")
    data = response.json()
    assert data["name"] == "John Smith"

def test_delete_customer(client: TestClient, test_db):
    response = client.delete("/customer/delete_customer/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Customer deleted successfully."}
    response = client.get("/customer/get_customer/1")
    assert response.status_code == 404

def test_load_json(client: TestClient, test_db):
    customer_data = [
        {"name": "Customer 1", "email": "customer1@example.com",
         "subscription_start_date": "2022-01-01", "subscription_end_date": "2023-01-01"},
        {"name": "Customer 2", "email": "customer2@example.com",
         "subscription_start_date": "2022-02-01", "subscription_end_date": "2023-02-01"}
    ]
    response = client.post("/customer/load_json/", json=customer_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Customers loaded successfully from JSON."}
    response = client.get("/customer/get_customer/2")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Customer 1"
    response = client.get("/customer/get_customer/3")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Customer 2"
