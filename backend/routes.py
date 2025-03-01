from fastapi import APIRouter
import joblib
from utils import preprocess_input

router = APIRouter()

model = joblib.load("../models/random_forest_model.pkl")

@router.post("/predict")
async def predict(data: dict):
    try:
        df = preprocess_input(data)
        prediction = model.predict(df)[0]
        return {"fraud" : bool(prediction)}

    except Exception as e:
        return {"error " : str(e)}



