from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['emotion_recommender']

# Clear existing products
db.products.delete_many({})
print("✓ Cleared existing products")

# Product data for all emotions
products = [
    # ===== HAPPY PRODUCTS =====
    {
        "name": "Wireless Party Speaker",
        "price": "$129.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400",
        "emotion": "happy",
        "description": "Portable speaker with LED lights"
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
    {
        "name": "LED Party Lights",
        "price": "$39.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1545269865-cbf237f9ef0b?w=400",
        "emotion": "happy",
        "description": "Colorful LED strip lights for parties"
    },
    {
        "name": "Happy Planner Journal",
        "price": "$19.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1514432324607-2e4c00038fee?w=400",
        "emotion": "happy",
        "description": "Positivity-focused planner and journal"
    },

    # ===== SAD PRODUCTS =====
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
    {
        "name": "Comfort Food Cookbook",
        "price": "$26.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400",
        "emotion": "sad",
        "description": "Recipes for comfort and warmth"
    },
    {
        "name": "Relaxation Candles",
        "price": "$24.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?w=400",
        "emotion": "sad",
        "description": "Scented candles for relaxation"
    },

    # ===== ANGRY PRODUCTS =====
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
    {
        "name": "Exercise Resistance Bands",
        "price": "$27.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1517836357463-d25ddfcbf042?w=400",
        "emotion": "angry",
        "description": "Set of resistance bands for workouts"
    },
    {
        "name": "Breathing Exercise App",
        "price": "$9.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1544716278-ca5e3af4abd8?w=400",
        "emotion": "angry",
        "description": "Guided breathing and meditation app"
    },

    # ===== NEUTRAL PRODUCTS =====
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
    {
        "name": "Reading Light",
        "price": "$32.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1578500494198-246f612d03b3?w=400",
        "emotion": "neutral",
        "description": "LED reading light with adjustable brightness"
    },
    {
        "name": "Notebook Set",
        "price": "$15.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1517433456452-f06b31d4a374?w=400",
        "emotion": "neutral",
        "description": "Set of quality notebooks for writing"
    },

    # ===== SURPRISE PRODUCTS =====
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
    {
        "name": "Lego Building Set",
        "price": "$79.99",
        "category": "Entertainment",
        "image": "https://images.unsplash.com/photo-1594787318286-3d835c1cab83?w=400",
        "emotion": "surprise",
        "description": "Advanced LEGO building set"
    },
    {
        "name": "Telescope",
        "price": "$149.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1608889335334-f3a84a66b18d?w=400",
        "emotion": "surprise",
        "description": "Powerful telescope for stargazing"
    },

    # ===== FEAR PRODUCTS =====
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
        "price": "$26.99",
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
    {
        "name": "Personal Alarm",
        "price": "$19.99",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=400",
        "emotion": "fear",
        "description": "Portable personal safety alarm"
    },
    {
        "name": "Protective Device Guide",
        "price": "$22.99",
        "category": "Books",
        "image": "https://images.unsplash.com/photo-1507842217343-583684f1e93c?w=400",
        "emotion": "fear",
        "description": "Guide to personal safety and protection"
    },

    # ===== DISGUST PRODUCTS =====
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
        "description": "Guide to simple and clean living"
    },
    {
        "name": "Natural Soap Collection",
        "price": "$32.99",
        "category": "Wellness",
        "image": "https://images.unsplash.com/photo-1600857062241-98e5bba06620?w=400",
        "emotion": "disgust",
        "description": "Organic handmade soaps"
    },
    {
        "name": "Water Filtration System",
        "price": "$89.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1579154204601-01d82b27c9d2?w=400",
        "emotion": "disgust",
        "description": "Advanced water purification system"
    },
    {
        "name": "Natural Detergent",
        "price": "$16.99",
        "category": "Home",
        "image": "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=400",
        "emotion": "disgust",
        "description": "Eco-friendly natural laundry detergent"
    }
]

# Insert products
result = db.products.insert_many(products)
print(f"\n✓ Inserted {len(result.inserted_ids)} products")

# Create indexes
db.products.create_index([("emotion", 1)])
db.products.create_index([("category", 1)])
print("✓ Created indexes")

# Verify data
print("\n📊 Products by emotion:")
emotion_count = db.products.aggregate([
    { "$group": { "_id": "$emotion", "count": { "$sum": 1 } } },
    { "$sort": { "count": -1 } }
])
for doc in emotion_count:
    print(f"   {doc['_id']}: {doc['count']} products")

print(f"\n✅ Database seeding complete!")
client.close()
