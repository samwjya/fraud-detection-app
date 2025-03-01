import pandas as pd 
from pydantic import BaseModel


def preprocess_input(data: dict):
    """ Convert input JSON data into a Pandas DataFrame for prediction. """
    try:
        df = pd.DataFrame([data])
        return df
    except Exception as e:
        raise ValueError(f"Invalid value data: {str(e)}")


class TranssactionModel(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float