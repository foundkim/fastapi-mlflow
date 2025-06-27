"""APIs for inference operations."""

from fastapi import APIRouter

from schemas import InferenceIn, InferenceOut

from services  import make_prediction

inference_router = APIRouter(prefix="/inference", tags=["Inference Operations"])


@inference_router.post("/predict", response_model=InferenceOut)
async def predict(inference_data: InferenceIn) -> InferenceOut:
    """Endpoint for making predictions based on input data."""
    
    # Here you would typically call your model's prediction method
    prediction = make_prediction(inference_data)
    

    return InferenceOut(species=prediction)


@inference_router.post("/bulk-predict", response_model=list[InferenceOut])
async def bulk_predict(inference_data: list[InferenceIn]) -> list[InferenceOut]:
    """Endpoint for making bulk predictions based on input data."""
    return []
