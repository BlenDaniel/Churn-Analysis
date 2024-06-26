from fastapi import FastAPI
from backend.api_service.endpoints import customer, visualization, dataset, analysis

app = FastAPI()

app.include_router(customer.router, prefix="/customer", tags=["Customer"])
app.include_router(visualization.router, prefix="/visualization", tags=["Visualization"])
app.include_router(dataset.router, prefix="/dataset", tags=["Dataset"])
app.include_router(analysis.router, prefix="/causal_inference", tags=["Causal Inference"])

