# backend/api_service/endpoints/visualization.py


from fastapi import APIRouter, Depends, HTTPException, Request
from requests import Session
from backend.config.logging import logger
from backend.analysis_tools.graphing import generate_graph
from backend.data_service.database import SessionLocal

router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/draw_graph/", response_model=None)
async def draw_graphs(data: Request, db: Session = Depends(get_db)):
    # Draw graphs and relationships
    try:
        # Call method from analysis_tools folder to generate graph
        graph_path = generate_graph(data, db)  # Assuming this function returns the path of the generated PNG file
        logger.info("Graphs drawn successfully.")
        return {"message": "Graphs drawn successfully.", "graph_path": graph_path}
    except Exception as e:
        logger.error(f"Error drawing graphs: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
