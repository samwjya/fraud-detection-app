from fastapi import APIRouter
import joblib
from utils import preprocess_input, TransactionModel

router = APIRouter()

model = joblib.load("../models/random_forest_model.pkl")

@router.post("/predict")
async def predict(data: TransactionModel):
    try:
        df = preprocess_input(data.dict())
        prediction = model.predict(df)[0]
        return {"fraud" : bool(prediction)}

    except Exception as e:
        return {"error " : str(e)}



