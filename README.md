# Churn Analysis Project

This project aims to analyze customer churn using causal inference techniques.

## Environment Setup

To set up the project environment, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/churn-analysis.git
```

2. Navigate to the project directory:

```bash
cd churn-analysis
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS and Linux:**

```bash
. venv/bin/activate
```

5. Install the project dependencies:

```bash
pip3 install -r requirements.txt
```

6. Start the FastAPI application: Run the FastAPI application using Uvicorn.

```bash
uvicorn backend.api_service.main:app --reload
```
This command starts the FastAPI application with auto-reload enabled. You can now access your API at http://localhost:8000.

With these instructions, you'll have your environment set up and your FastAPI application running. Let me know if you need further assistance!

## Project Structure

The project directory structure is as follows:
```
churn_analysis/
│
├── backend/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py      # Application settings
│   │   └── logging.py       # Logging configuration
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── cache.py         # Caching utilities
│   │   └── authentication.py  # User authentication utilities
│   │
│   ├── api_service/
│   │   ├── __init__.py
│   │   └── main.py         # FastAPI routes
│   │
│   ├── data_service/
│   │   ├── __init__.py
│   │   ├── database.py     # Database access and ORM
│   │   └── models.py       # ORM models
│   │
│   └── causal_inference_service/
│       ├── __init__.py
│       └── causal_analysis.py    # Causal inference using DoWhy
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Application pages
│   │   └── utils/         # Utility functions
│   ├── package.json       # Frontend dependencies
│   ├── README.md
│   └── ...                # Other frontend files
│
├── docker/
│   ├── api_service.dockerfile
│   ├── data_service.dockerfile
│   └── frontend.dockerfile
│
├── tests/
│   ├── api_service/
│   ├── data_service/
│   ├── causal_inference_service/
│   └── frontend/
│
├── requirements.txt    # Python dependencies
├── README.md
└── .gitignore

```


## Requirements

- Python 3.9 or higher

## Running the Application

To run the application, follow these steps:

1. Start the backend services:

```bash
# Navigate to the churn_analysis directory
cd churn_analysis

# Start the API service
uvicorn api_service.main:app --host 0.0.0.0 --port 8000
```

2. Start the frontend application:

```bash
# Navigate to the frontend directory
cd churn_analysis/frontend

# Install dependencies
npm install

# Start the frontend server
npm start
```

The application will be accessible at `http://localhost:3000` by default.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.