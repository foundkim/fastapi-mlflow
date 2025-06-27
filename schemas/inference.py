"""Inference schemas module"""

from pydantic import BaseModel


class InferenceIn(BaseModel):
    """Schema for inference input data."""

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class InferenceOut(BaseModel):
    """Schema for inference output data."""

    species: str
