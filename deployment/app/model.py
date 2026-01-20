import torch
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification

MODEL_PATH = "models/bert_sentiment_gpu"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
model.to(device)
model.eval()

label_map = {0: "negative", 1: "neutral", 2: "positive"}


def predict_sentiment(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1).cpu().numpy()[0]

    predicted_label = label_map[int(np.argmax(probs))]
    confidence = float(np.max(probs))

    return {
        "sentiment": predicted_label,
        "confidence": round(confidence, 4),
        "probabilities": {
            label_map[i]: round(float(probs[i]), 4)
            for i in range(len(probs))
        }
    }