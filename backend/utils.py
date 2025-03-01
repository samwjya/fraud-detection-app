import pandas as pd 
def preprocess_input(data: dict):
    """ Convert input JSON data into a Pandas DataFrame for prediction. """
    try:
        df = pd.DataFrame([data])
        return df
    except Exception as e:
        raise ValueError(f"Invalid value data: {str(e)}")