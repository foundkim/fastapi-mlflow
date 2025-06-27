"""Machine Learning Services Module for Inference"""

import pandas as pd
from schemas import InferenceIn

from .model import get_model


def make_prediction(inference_data: InferenceIn):
    """Predict the species based on input data."""

    input_df = pd.DataFrame(inference_data.model_dump(mode="python"))
    
    input_df = input_df.rename(
        columns={
            # For compatibility with the model's expected input
            
            # Adam
            "sepal_length": "sepal length(cm)",
            
            # Paul
            "sepal_width": "sepal.width",
            "petal_length": "petal_length_cm",
            "petal_width": "petal_width_cm",
        }
    )
    
    # for Paul
    input_df['Unnaned: 0'] = [0]

    model = get_model()

    prediction = model.predict(input_df)

    return prediction.tolist()[0]
