# Flipkart Reviews Sentiment Analysis – FastAPI Deployment

##  Overview

This project deploys a **BERT-based sentiment analysis model** as a **high-performance REST API** using **FastAPI**.
The model classifies Flipkart product reviews into:
*  **Negative**
*  **Neutral**
*  **Positive**

The API is **GPU-aware**, **low-latency**, and designed following **production ML best practices**.

---

##  Model Details

* **Model:** `bert-base-uncased`
* **Framework:** Hugging Face Transformers (PyTorch)
* **Classes:** Negative, Neutral, Positive
* **Training:** Fine-tuned on 180K+ Flipkart reviews
* **Performance:**
  * Accuracy: **98.5%**
  * Macro F1-score: **0.97**

---

##  Setup Instructions

###  Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

---

###  Install Dependencies

```bash
pip install -r requirements.txt
```
---

##  Run the API

From the `deployment/` directory:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

##  API Documentation (Swagger UI)

Once running, open:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints

###  Health Check

```
GET /
```

**Response**

```json
{
  "status": "running",
  "model": "bert-base-uncased",
  "task": "Sentiment Analysis"
}
```

---

###  Sentiment Prediction

```
POST /predict
```

**Request Body**

```json
{
  "text": "The product quality is amazing and totally worth the price"
}
```

**Response**

```json
{
  "sentiment": "positive",
  "confidence": 0.97,
  "probabilities": {
    "negative": 0.01,
    "neutral": 0.02,
    "positive": 0.97
  }
}
```

---
