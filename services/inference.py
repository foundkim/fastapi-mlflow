"""Machine Learning Services Module for Inference"""

import pandas as pd
from schemas import InferenceIn, InferenceOut

from core.log import logger
from .model import get_model

SPECIES = ["setosa", "versicolor", "virginica"]


def make_prediction(inference_data: InferenceIn):
    """Predict the species based on input data."""

    input_df = pd.DataFrame([inference_data.model_dump(mode="python")])

    # input_df = input_df.rename(
    #     columns={
    #         # For compatibility with the model's expected input
    #         # Adam
    #         "sepal_length": "sepal length(cm)",
    #         # Paul
    #         "sepal_width": "sepal.width",
    #         "petal_length": "petal_length_cm",
    #         "petal_width": "petal_width_cm",
    #     }
    # )

    # for Paul
    # input_df["Unnaned: 0"] = [0]

    model = get_model()
    
    logger.info("Model loaded successfully.")
    
    logger.error("Input Data: %s", input_df.to_dict(orient="records")[0])
    logger.debug("Input DataFrame:\n%s", input_df)
    logger.warning("Preparing to make prediction.")
    prediction = model.predict(input_df)

    log_df = input_df.copy()
    log_df["prediction"] = prediction.tolist()[0]

    logger.info("Prediction made: %s", log_df.to_dict(orient="records")[0])

    return InferenceOut(
        **inference_data.model_dump(mode="python"),
        species=SPECIES[prediction.tolist()[0]],
    )
