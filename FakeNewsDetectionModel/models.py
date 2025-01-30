import joblib
import numpy as np

model = None
vectorizer = None

def init_model(app):
    global model, vectorizer
    model = joblib.load('app/fake_news_model/model.pkl')  # Load trained model
    vectorizer = joblib.load('app/fake_news_model/vectorizer.pkl')  # Load vectorizer


def predict_news(article):
    article_vectorized = vectorizer.transform([article])
    prediction = model.predict(article_vectorized)
    return 'fake' if prediction == 0 else 'real'
