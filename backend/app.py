from fastapi import FastAPI 
from routes import router
import uvicorn
import os

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "🚀 Fraud Detection API is up and running!"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))


