from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# Initialize FastAPI app and router
app = FastAPI()
router = APIRouter()

# Load model
model = joblib.load("models/random_forest_model.pkl")

# Pydantic model
class TransactionModel(BaseModel):
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

# Preprocess function
def preprocess_input(data: dict):
    try:
        df = pd.DataFrame([data])
        return df
    except Exception as e:
        raise ValueError(f"Invalid value data: {str(e)}")

# API routes
@app.get("/")
def read_root():
    return {"message": "🚀 Fraud Detection API is up and running!"}

@app.post("/predict")
async def predict(data: TransactionModel):
    try:
        df = preprocess_input(data.dict())
        prediction = model.predict(df)[0]
        return {"fraud": bool(prediction)}
    except Exception as e:
        return {"error": str(e)}

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))

