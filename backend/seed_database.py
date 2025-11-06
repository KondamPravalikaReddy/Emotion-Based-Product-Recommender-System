from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['emotion_recommender']

# Clear existing data
print("Clearing existing collections...")
db.products.delete_many({})
db.emotion_history.delete_many({})

# Sample products data
products = [
    # Happy products
    {
        "name": "Wireless Party Speaker",
        "price": "$129.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400",
        "emotion": "happy",
        "description": "Portable speaker with LED lights and 360° sound"
    },
    {
        "name": "Colorful Running Shoes",
        "price": "$89.99",
        "category": "Fashion",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
        "emotion": "happy",
        "description": "Comfortable running shoes in vibrant colors"
    },
    {
        "name": "Board Game Collection",
        "price": "$45.99",
        "category": "Entertainment",
        "image": "https://images.unsplash.com/photo-1632501641765-e568d28b0015?w=400",
        "emotion": "happy",
        "description": "Fun games for family and friends"
    },
    {
        "name": "Gourmet Chocolate Box",
        "price": "$34.99",
        "category": "Food",
        "image": "https://images.unsplash.com/photo-1511381939415-e44015466834?w=400",
        "emotion": "happy",
        "description": "Premium assorted chocolates"
    },
    {
        "name": "Tropical Vacation Guide",
        "price": "$24.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400",
        "emotion": "happy",
        "description": "Inspiring travel destination guide"
    },
    {
        "name": "Yoga Mat & Accessories",
        "price": "$59.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400",
        "emotion": "happy",
        "description": "Premium yoga mat with carrying strap"
    },

    # Sad products
    {
        "name": "Comfort Blanket",
        "price": "$49.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=400",
        "emotion": "sad",
        "description": "Ultra-soft weighted blanket"
    },
    {
        "name": "Self-Care Journal",
        "price": "$19.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400",
        "emotion": "sad",
        "description": "Guided journal for mindfulness and reflection"
    },
    {
        "name": "Aromatherapy Diffuser",
        "price": "$39.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=400",
        "emotion": "sad",
        "description": "Essential oil diffuser for relaxation"
    },
    {
        "name": "Herbal Tea Collection",
        "price": "$29.99",
        "category": "Food",
        "image": "https://images.unsplash.com/photo-1597318112051-6f36d4363446?w=400",
        "emotion": "sad",
        "description": "Calming herbal tea selection"
    },
    {
        "name": "Meditation Cushion",
        "price": "$44.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=400",
        "emotion": "sad",
        "description": "Comfortable meditation support cushion"
    },
    {
        "name": "Cozy Slippers",
        "price": "$34.99",
        "category": "Fashion",
        "image": "https://images.unsplash.com/photo-1643123831634-dfe68a04b88e?w=400",
        "emotion": "sad",
        "description": "Warm and cozy indoor slippers"
    },

    # Angry products
    {
        "name": "Stress Relief Ball",
        "price": "$14.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1599058917212-d750089bc07e?w=400",
        "emotion": "angry",
        "description": "Squeeze ball for stress relief"
    },
    {
        "name": "Punching Bag Set",
        "price": "$149.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?w=400",
        "emotion": "angry",
        "description": "Home boxing setup for workouts"
    },
    {
        "name": "Calming Music Album",
        "price": "$12.99",
        "category": "Entertainment",
        "image": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=400",
        "emotion": "angry",
        "description": "Soothing instrumental music collection"
    },
    {
        "name": "Mindfulness Book",
        "price": "$22.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1505664194779-8beaceb93744?w=400",
        "emotion": "angry",
        "description": "Learn anger management techniques"
    },
    {
        "name": "Lavender Essential Oil",
        "price": "$18.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=400",
        "emotion": "angry",
        "description": "Pure lavender oil for relaxation"
    },
    {
        "name": "Zen Garden Kit",
        "price": "$32.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=400",
        "emotion": "angry",
        "description": "Meditative sand garden for stress relief"
    },

    # Neutral products
    {
        "name": "Smart Watch",
        "price": "$199.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
        "emotion": "neutral",
        "description": "Feature-rich smartwatch with health tracking"
    },
    {
        "name": "Classic White Shirt",
        "price": "$49.99",
        "category": "Fashion",
        "image": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=400",
        "emotion": "neutral",
        "description": "Timeless wardrobe essential"
    },
    {
        "name": "Coffee Maker",
        "price": "$79.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=400",
        "emotion": "neutral",
        "description": "Programmable coffee machine"
    },
    {
        "name": "Productivity Planner",
        "price": "$27.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=400",
        "emotion": "neutral",
        "description": "Daily planner for organization"
    },
    {
        "name": "Desk Organizer",
        "price": "$35.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1565166937231-94704f628524?w=400",
        "emotion": "neutral",
        "description": "Multi-compartment desk organizer"
    },
    {
        "name": "Water Bottle",
        "price": "$24.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400",
        "emotion": "neutral",
        "description": "Reusable stainless steel water bottle"
    },

    # Surprise products
    {
        "name": "Mystery Box Subscription",
        "price": "$99.99",
        "category": "Entertainment",
        "image": "https://images.unsplash.com/photo-1513885535751-8b9238bd345a?w=400",
        "emotion": "surprise",
        "description": "Monthly surprise box delivery"
    },
    {
        "name": "VR Headset",
        "price": "$299.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1592478411213-6153e4ebc07d?w=400",
        "emotion": "surprise",
        "description": "Immersive virtual reality experience"
    },
    {
        "name": "Magic Trick Set",
        "price": "$39.99",
        "category": "Entertainment",
        "image": "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=400",
        "emotion": "surprise",
        "description": "Professional magic tricks kit"
    },
    {
        "name": "Exotic Spice Collection",
        "price": "$44.99",
        "category": "Food",
        "image": "https://images.unsplash.com/photo-1596040033229-a0b34c5fc345?w=400",
        "emotion": "surprise",
        "description": "International spice selection"
    },
    {
        "name": "Science Experiment Kit",
        "price": "$54.99",
        "category": "Entertainment",
        "image": "https://images.unsplash.com/photo-1567427018141-0584cfcbf1b8?w=400",
        "emotion": "surprise",
        "description": "Educational science experiments"
    },
    {
        "name": "Unique Gadget Collection",
        "price": "$89.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1550009158-9ebf69173e03?w=400",
        "emotion": "surprise",
        "description": "Innovative gadgets and tools"
    },

    # Fear products
    {
        "name": "Night Light",
        "price": "$24.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1573920111312-04ec60d8e6c5?w=400",
        "emotion": "fear",
        "description": "Soothing ambient night light"
    },
    {
        "name": "Security Camera",
        "price": "$129.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?w=400",
        "emotion": "fear",
        "description": "Smart home security camera"
    },
    {
        "name": "Comfort Food Cookbook",
        "price": "$29.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400",
        "emotion": "fear",
        "description": "Recipes for comfort and warmth"
    },
    {
        "name": "Weighted Blanket",
        "price": "$89.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=400",
        "emotion": "fear",
        "description": "Calming weighted blanket"
    },
    {
        "name": "Calming Tea Set",
        "price": "$34.99",
        "category": "Food",
        "image": "https://images.unsplash.com/photo-1597318112051-6f36d4363446?w=400",
        "emotion": "fear",
        "description": "Relaxation tea selection"
    },
    {
        "name": "Relaxation App Subscription",
        "price": "$49.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400",
        "emotion": "fear",
        "description": "Premium meditation and relaxation app"
    },

    # Disgust products
    {
        "name": "Air Purifier",
        "price": "$159.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400",
        "emotion": "disgust",
        "description": "HEPA filter air purification system"
    },
    {
        "name": "Organic Cleaning Set",
        "price": "$44.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=400",
        "emotion": "disgust",
        "description": "Eco-friendly cleaning products"
    },
    {
        "name": "Essential Oil Kit",
        "price": "$39.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=400",
        "emotion": "disgust",
        "description": "Fresh-scented essential oils"
    },
    {
        "name": "Fresh Linen Spray",
        "price": "$19.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=400",
        "emotion": "disgust",
        "description": "Refreshing fabric spray"
    },
    {
        "name": "Minimalist Lifestyle Book",
        "price": "$26.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400",
        "emotion": "disgust",
        "description": "Guide to simple living"
    },
    {
        "name": "Natural Soap Collection",
        "price": "$32.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1600857062241-98e5bba06620?w=400",
        "emotion": "disgust",
        "description": "Organic handmade soaps"
    }
]

# Insert products
print(f"Inserting {len(products)} products...")
result = db.products.insert_many(products)
print(f"✓ Inserted {len(result.inserted_ids)} products")

# Create indexes
print("Creating indexes...")
db.products.create_index([("emotion", 1)])
db.products.create_index([("category", 1)])
db.emotion_history.create_index([("user_id", 1), ("timestamp", -1)])
print("✓ Indexes created")

print("\n✅ Database seeded successfully!")
print(f"📊 Total products: {db.products.count_documents({})}")
print("\nAvailable emotions:")
emotions = db.products.distinct('emotion')
for emotion in sorted(emotions):
    count = db.products.count_documents({'emotion': emotion})
    print(f"  • {emotion}: {count} products")

print("\nAvailable categories:")
categories = db.products.distinct('category')
for category in sorted(categories):
    count = db.products.count_documents({'category': category})
    print(f"  • {category}: {count} products")

client.close()
