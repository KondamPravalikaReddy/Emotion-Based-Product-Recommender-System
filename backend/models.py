from datetime import datetime
from pymongo import ASCENDING, DESCENDING

class Product:
    """Product model"""
    
    def __init__(self, name, price, category, image, emotion, description=''):
        self.name = name
        self.price = price
        self.category = category
        self.image = image
        self.emotion = emotion
        self.description = description
        self.created_at = datetime.utcnow()
    
    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'image': self.image,
            'emotion': self.emotion,
            'description': self.description,
            'created_at': self.created_at
        }

class EmotionHistory:
    """Emotion history model"""
    
    def __init__(self, user_id, emotion, confidence):
        self.user_id = user_id
        self.emotion = emotion
        self.confidence = confidence
        self.timestamp = datetime.utcnow()
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'emotion': self.emotion,
            'confidence': self.confidence,
            'timestamp': self.timestamp
        }
