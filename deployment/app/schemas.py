from pydantic import BaseModel, Field

class ReviewRequest(BaseModel):
    text: str = Field(
        ..., 
        example="The product quality is amazing and totally worth the price"
    )

class PredictionResponse(BaseModel):
    sentiment: str
    confidence: float
    probabilities: dict