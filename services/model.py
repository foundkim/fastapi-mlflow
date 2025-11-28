"""Load MLFlow Models"""

import mlflow
from core import config

# mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)

def get_model():
    """
    Load a model from MLFlow.
    """
    
    mlflow.set_tracking_uri(config.MLFLOW_TRACKING_URI)
    
    return mlflow.pyfunc.load_model(model_uri=config.MLFLOW_MODEL_URI)

