# backend/api_service/endpoints/visualization.py

from fastapi import APIRouter, HTTPException, Depends
from backend.config.logging import logger
from backend.analysis_tools.graphing import generate_graph

router = APIRouter()

@router.get("/draw_graphs/")
async def draw_graphs():
    # Draw graphs and relationships
    try:
        # Call method from analysis_tools folder to generate graph
        graph_path = generate_graph()  # Assuming this function returns the path of the generated PNG file
        logger.info("Graphs drawn successfully.")
        return {"message": "Graphs drawn successfully.", "graph_path": graph_path}
    except Exception as e:
        logger.error(f"Error drawing graphs: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
