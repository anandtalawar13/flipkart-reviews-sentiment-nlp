from fastapi import FastAPI
from app.schemas import ReviewRequest, PredictionResponse
from app.model import predict_sentiment

app = FastAPI(
    title="Flipkart Review Sentiment API",
    description="BERT-based Sentiment Analysis API (Negative / Neutral / Positive)",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "running",
        "model": "bert-base-uncased",
        "task": "Sentiment Analysis"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: ReviewRequest):
    return predict_sentiment(request.text)