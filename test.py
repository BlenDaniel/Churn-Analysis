import psycopg2

try:
    # Connect to the database
    conn = psycopg2.connect(
        dbname='customers',
        user='postgres',
        password='password!',
        host='localhost',
        port='5432'
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT version();")

    # Fetch result
    db_version = cur.fetchone()
    print("PostgreSQL database version:", db_version)

except Exception as e:
    print("Error:", e)

finally:
    # Close communication with the database
    if conn:
        conn.close()


'''



# Function to add a customer entry
def add_customer(db: Session, name: str, email: str, subscription_start_date: date, subscription_end_date: date, churned: bool = False):
    customer = CustomerInitial(name=name, email=email, subscription_start_date=subscription_start_date, subscription_end_date=subscription_end_date, churned=churned)
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

@router.get("/check_database_connection/", response_model=ApiResponse)
async def check_database_connection(db: Session = Depends(get_db)):
    try:
       # Call the add_customer function with the required parameters
        new_customer = add_customer(
            db=db,
            name="John Doe",
            email="john.doe@saa.com",
            subscription_start_date=date(2023, 6, 1),
            subscription_end_date=date(2024, 6, 1),
            churned=False
        )
        # Print the added customer details
        print(f"Added customer: {new_customer.name} ({new_customer.email})")

         # Attempt a simple query to check if the database is connected
        query = select(CustomerInitial.id).limit(1)  # Select the id column from the Customer table
        result = db.execute(query).fetchone()  # Execute the query
        if result:
            return {"message": "Database connection is successful."}
        else:
            return {"message": "No data found in the database."}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Database connection error")


'''