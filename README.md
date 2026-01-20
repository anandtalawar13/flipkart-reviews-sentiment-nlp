#  Flipkart Reviews Sentiment Analysis (NLP + BERT)

An end-to-end **Sentiment Analysis system** built on **180K+ Flipkart product reviews**, covering the full ML lifecycle — from data cleaning and classical NLP models to **transformer-based BERT**, API deployment, and Dockerization.

---

##  Problem Statement
E-commerce platforms receive millions of short, noisy reviews.  
The goal of this project is to **accurately classify customer sentiment** into:
- 🔴 Negative  
- 🟡 Neutral  
- 🟢 Positive  

with high precision and real-world deployability.

---

##  Dataset
- **Source:** Kaggle – Flipkart Product Reviews  
- **Size:** ~205,000 raw reviews  
- **Usable reviews after cleaning:** ~180,000  

**Key characteristics:**
- Very short text (avg. 3–4 words)
- High class imbalance (positive-heavy)
- Neutral sentiment is linguistically ambiguous

---

##  Data Processing
- Removed null / empty reviews safely (no aggressive filtering)
- Text normalization & cleaning for classical models
- Preserved raw text for transformer-based models
- Stratified train–test splits to maintain class distribution

---

##  Models Implemented

### 1️. Classical NLP Models
- Logistic Regression (baseline)
- Linear SVM (best classical performer)
- XGBoost (high-precision alternative)

### 2️. Transformer Model
- **BERT (`bert-base-uncased`)**
- Fine-tuned using Hugging Face Transformers
- GPU-aware training and inference
- Mixed precision (FP16) support

---

##  Model Performance Comparison

| Model | Accuracy | Macro F1 |
|------|---------|----------|
| Logistic Regression | 93% | 0.88 |
| Linear SVM | 96% | 0.93 |
| XGBoost | 97% | 0.93 |
| **BERT (Final)** | **98.5%** | **0.97**  |

**Key Insight:**  
Classical models struggled with **neutral sentiment ambiguity**, which was significantly improved using BERT’s contextual understanding.

---

##  Deployment

###  FastAPI
- Clean REST API for inference
- Confidence scores + class probabilities
- GPU/CPU auto-detection
- Swagger UI for testing

###  Docker
- Fully containerized deployment
- Portable across environments
- GPU-enabled via NVIDIA runtime

Deployment code is available in:
```

/deployment

````

---

##  Example API Request

```json
POST /predict
{
  "text": "Not bad, but expected better quality"
}
````

### Response

```json
{
  "sentiment": "neutral",
  "confidence": 0.91,
  "probabilities": {
    "negative": 0.04,
    "neutral": 0.91,
    "positive": 0.05
  }
}
```

---

## Author

**Ananda Siddappa Talawar**
Data Scientist | ML Engineer

* GitHub: [https://github.com/anandtalawar13](https://github.com/anandtalawar13)
* LinkedIn: [https://www.linkedin.com/in/anand-talawar-83b1a9127/](https://www.linkedin.com/in/anand-talawar-83b1a9127/)

---
⭐ If you found this project useful, feel free to star the repository!
