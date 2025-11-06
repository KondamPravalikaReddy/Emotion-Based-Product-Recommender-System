from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from deepface import DeepFace
import base64
from PIL import Image
import io
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def decode_base64_image(base64_string, save_path="temp_image.jpg"):
    try:
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        image_bytes = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        image.save(save_path)
        return save_path
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return None

app = Flask(__name__)
CORS(app)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/emotion_recommender'
mongo = PyMongo(app)
db = mongo.db

@app.route('/api/detect-emotion', methods=['POST'])
def detect_emotion():
    try:
        data = request.json
        if not data or 'image' not in data:
            return jsonify({'error': 'No image'}), 400

        temp_path = decode_base64_image(data['image'])
        if not temp_path:
            return jsonify({'error': 'Invalid image'}), 400

        result = DeepFace.analyze(temp_path, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list):
            result = result[0]

        emotions = result['emotion']
        dominant_emotion = result['dominant_emotion']
        confidence = float(emotions[dominant_emotion]) / 100

        products = list(db.products.find({'emotion': dominant_emotion}).limit(12))
        formatted_products = []
        for p in products:
            formatted_products.append({
                'id': str(p['_id']),
                'name': p['name'],
                'price': float(p['price'].replace('$', '')) if isinstance(p['price'], str) else p['price'],
                'category': p['category'],
                'image': p['image'],
                'emotion': p['emotion']
            })

        if os.path.exists(temp_path):
            os.remove(temp_path)

        logger.info(f"Emotion: {dominant_emotion}, Products: {len(formatted_products)}")

        return jsonify({
            'emotion': dominant_emotion,
            'confidence': round(confidence, 2),
            'all_emotions': {k: float(v) for k, v in emotions.items()},
            'products': formatted_products
        }), 200

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/categories', methods=['GET'])
def get_categories():
    try:
        categories = db.products.distinct('category')
        return jsonify({'categories': ['All'] + sorted(categories)}), 200
    except:
        return jsonify({'categories': ['All']}), 200

@app.route('/api/health', methods=['GET'])
def health():
    try:
        db.command('ping')
        return jsonify({'status': 'ok'}), 200
    except:
        return jsonify({'status': 'error'}), 500

if __name__ == '__main__':
    logger.info("Backend starting...")
    app.run(debug=True, host='0.0.0.0', port=5000)
