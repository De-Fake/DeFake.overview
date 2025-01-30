from flask import request, jsonify
from models import predict_news
def init_routes(app):
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json()
        article = data.get('article', '')

        if not article:
            return jsonify({'error': 'No article provided'}), 400

        result = predict_news(article)
        return jsonify({'prediction': result})
