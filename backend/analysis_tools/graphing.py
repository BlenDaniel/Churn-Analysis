# backend/analysis_tools/database.py

import os
from fastapi import HTTPException, Request
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from backend.config.settings import settings
from backend.config.logging import logger
import pandas as pd
from sqlalchemy.orm import Session
from backend.data_service.models import Customer


# Create resources folder if it doesn't exist
if not os.path.exists("resources"):
    os.makedirs("resources")

    
def generate_graph_with_specifics(data: Request, db: Session):
    try:
        # Connect to the database and inspect the columns
        inspector = inspect(db.bind)
        columns = inspector.get_columns('customers')  # Assuming 'customers' is the table name
        column_names = [column['name'] for column in columns]

        # Check if the data can be mapped to any column
        valid_data = {}
        for item in data.query_params:
            key = item
            value = data.query_params[item]
            if key in column_names:
                valid_data[key] = value

        if not valid_data:
            raise HTTPException(status_code=400, detail="No valid data to map to database columns.")

        # Convert valid_data to DataFrame
        df = pd.DataFrame([valid_data])

        # Plot the data
        ax = df.plot(kind='bar', figsize=(10, 6))
        plt.title('Generated Graph')
        plt.xlabel('Data Points')
        plt.ylabel('Values')

        # Save the plot as an image in the resources folder with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = os.path.join("resources", f"generated_graph_{timestamp}.png")
        plt.savefig(image_path)
        plt.close()

        return {"message": "Graph generated and saved successfully.", "image_path": image_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error generating graph.")


def generate_graph(data: Request, db: Session):



    customers = db.query(Customer).all()
    if not customers:
        raise ValueError("No data found in the database.")

    data = {
        "subscription_start_date": [customer.subscription_start_date for customer in customers],
        "subscription_end_date": [customer.subscription_end_date for customer in customers],
        "churned": [customer.churned for customer in customers]
    }

    df = pd.DataFrame(data)
    df['subscription_duration'] = (df['subscription_end_date'] - df['subscription_start_date']).dt.days

    plt.figure(figsize=(10, 6))
    plt.hist(df['subscription_duration'], bins=30, edgecolor='k', alpha=0.7)
    plt.xlabel('Subscription Duration (days)')
    plt.ylabel('Number of Customers')
    plt.title('Customer Subscription Duration Histogram')

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    image_path = f"resources/subscription_duration_{timestamp}.png"
    plt.savefig(image_path)
    plt.close()
    return image_path
