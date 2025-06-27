"""App Main"""

from fastapi import FastAPI
import uvicorn


from api import inference_router, home_router

from core import config


app = FastAPI(
    title=config.APP_NAME,
    description=config.APP_DESCRIPTION,
    version=config.APP_VERSION,
)


app.include_router(inference_router)
app.include_router(home_router)


if __name__ == "__main__":
    # Run the application using uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
