"""Inference schemas module"""

from pydantic import BaseModel


class InferenceIn(BaseModel):
    """Schema for inference input data."""

    sepal_lenght: float
    sepal_width: float
    petal_lenght: float
    petal_width: float


class InferenceOut(InferenceIn):
    """Schema for inference output data."""

    species: str
