# backend/api_service/endpoints/causal_inference.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.config.logging import logger
from backend.data_service.database import SessionLocal
from backend.data_service.models import ApiResponse
import pandas as pd
import numpy as np
import pygraphviz
import matplotlib.pyplot as plt
import dowhy
import networkx as nx
from dowhy import CausalModel
from dowhy import gcm


router = APIRouter()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/effect_estimation/", response_model=ApiResponse)
async def estimate_effect(model_spec: dict, db: Session = Depends(get_db)):
    try:
        dataset = pd.DataFrame(model_spec["data"])
        causal_graph = model_spec["causal_graph"]
        treatment = model_spec["treatment"]
        outcome = model_spec["outcome"]

        model = dowhy.CausalModel(
            data=dataset,
            graph=causal_graph.replace("\n", " "),
            treatment=treatment,
            outcome=outcome
        )
        model.view_model(layout='dot', file_name="causal_model_q1", size=(30, 15))
        identified_estimand = model.identify_effect(proceed_when_unidentifiable=True, method_name="maximal-adjustment")
        causal_estimate = model.estimate_effect(identified_estimand, test_significance=True, method_name="backdoor.linear_regression")
        
        logger.info(f"Causal Estimate: {causal_estimate.value}")
        return {"message": f"Causal Estimate is {causal_estimate.value}"}
    except Exception as e:
        logger.error(f"Error estimating causal effect: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
