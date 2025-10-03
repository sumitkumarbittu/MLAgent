# app.py - Sentiment Analysis API using Sentence Embeddings + Logistic Regression
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import joblib
import os
import sys
from sentence_transformers import SentenceTransformer
import numpy as np

# -------------------------
# Initialize FastAPI
# -------------------------
app = FastAPI(
    title="Sentiment Analysis API",
    description="Sentiment analysis API using sentence embeddings + Logistic Regression",
    version="1.0.0"
)

# -------------------------
# CORS middleware
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Request models
# -------------------------
class TextRequest(BaseModel):
    text: str

class BatchRequest(BaseModel):
    texts: List[str]

# -------------------------
# Load models safely
# -------------------------
try:
    model_path = os.path.join(os.path.dirname(__file__), "model1.pkl")
    print(f"Loading classifier from: {model_path}")
    classifier = joblib.load(model_path)
    print("Classifier loaded successfully.")

    print("Loading sentence transformer model...")
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    print("Sentence transformer loaded successfully.")
except Exception as e:
    print("Critical Error: Failed to load models:", repr(e))
    sys.exit(1)

# -------------------------
# Prediction function
# -------------------------
def predict_sentiment_ml(text: str) -> dict:
    """
    Generate sentence embedding for text and predict sentiment.
    Ensures embeddings are 2D arrays.
    """
    try:
        # Convert to 2D array
        embedding = embed_model.encode([text])
        if len(embedding.shape) == 1:
            embedding = embedding.reshape(1, -1)

        pred = classifier.predict(embedding)[0]
        sentiment = "positive" if int(pred) == 1 else "negative"
        return {"prediction": int(pred), "sentiment": sentiment}
    except Exception as e:
        print(f"Error predicting text '{text}': {repr(e)}")
        raise

# -------------------------
# API endpoints
# -------------------------
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is running"}

@app.post("/predict")
async def predict_sentiment(req: TextRequest):
    try:
        result = predict_sentiment_ml(req.text)
        return {
            "text": req.text,
            "prediction": result["prediction"],
            "sentiment": result["sentiment"],
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

@app.post("/predict_batch")
async def predict_batch_sentiment(req: BatchRequest):
    try:
        texts = req.texts
        if not texts:
            raise HTTPException(status_code=400, detail="No texts provided")
        
        # Generate embeddings for all texts at once for efficiency
        embeddings = embed_model.encode(texts)
        if len(embeddings.shape) == 1:
            embeddings = embeddings.reshape(1, -1)

        predictions = classifier.predict(embeddings)
        results = []
        for text, pred in zip(texts, predictions):
            sentiment = "positive" if int(pred) == 1 else "negative"
            results.append({
                "text": text,
                "prediction": int(pred),
                "sentiment": sentiment
            })
            
        return {
            "predictions": results,
            "count": len(results),
            "status": "success"
        }
    except Exception as e:
        print(f"Batch prediction error: {repr(e)}")
        raise HTTPException(status_code=500, detail=f"Batch prediction failed: {e}")

# -------------------------
# Run the API
# -------------------------
if __name__ == "__main__":
    import uvicorn
    print("Starting server on http://127.0.0.1:8000")
    print("API documentation available at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)