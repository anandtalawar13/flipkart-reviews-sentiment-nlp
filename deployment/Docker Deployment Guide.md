````md
# 🐳 Docker Deployment Guide – Flipkart Sentiment Analysis API
---


⚠️ **Important:**
The `models/bert_sentiment_gpu/` directory must contain the **saved BERT model and tokenizer files**.

---

##  Step 1: Build the Docker Image

From inside the directory, run:

```bash
docker build -t flipkart-sentiment-api .
```

This will:
* Install dependencies
* Copy application code and model
* Create a runnable Docker image

---

##  Step 2: Run the Container (CPU)

```bash
docker run -p 8000:8000 flipkart-sentiment-api
```

* Maps container port `8000` to local port `8000`
* Starts the FastAPI server

---

##  Step 3: Run with GPU (Optional)

```bash
docker run --gpus all -p 8000:8000 flipkart-sentiment-api
```

The application automatically detects GPU availability:

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```
---

##  Step 4: Access the API

### Swagger UI 

Open your browser and go to:

```
http://localhost:8000/docs
```

This provides:
* Interactive API documentation
* Easy testing of endpoints
* Clean demo for recruiters and reviewers

---

##  API Endpoints

###  Health Check

**GET /**

```json
{
  "status": "running",
  "model": "bert-base-uncased",
  "task": "Sentiment Analysis"
}
```

---

###  Predict Sentiment

**POST /predict**

#### Request

```json
{
  "text": "The product quality is amazing and totally worth the price"
}
```

#### Response

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

##  Stop the Container

Press:

```
CTRL + C
```

Or stop it manually:

```bash
docker ps
docker stop <container_id>
```

---

##  Common Issues & Fixes

### ❌ Port already in use

Run on a different port:

```bash
docker run -p 8001:8000 flipkart-sentiment-api
```
Then access:

```
http://localhost:8001/docs
```

---