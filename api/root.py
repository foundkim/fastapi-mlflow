"""Home page for the API."""

from fastapi import APIRouter

home_router = APIRouter(prefix="", tags=["Home Page"])


@home_router.get("/")
async def read_root() -> dict:
    """Root endpoint for the API."""
    
    return {"message": "Welcome to the FastAPI MFlow application!"}
