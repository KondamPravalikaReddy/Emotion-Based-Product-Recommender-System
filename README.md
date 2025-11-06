# 🎭 Emotion-Based Product Recommender System

A full-stack web application that detects user emotions through facial recognition and recommends personalized products based on their emotional state.

---

## 💡 Why It’s Needed in Today’s World

In today’s fast-paced digital world, **understanding human emotions** has become crucial for building **personalized and meaningful user experiences**.  
Traditional e-commerce platforms recommend products purely based on **search history or user behavior**, but they **ignore emotional context** — a key factor that influences buying decisions.

The **Emotion-Based Product Recommender System** bridges this gap by using **AI-driven emotion detection** to tailor product suggestions in real-time.  

### 🌍 Real-World Importance
- 🧠 **Human-Centered AI**: Enhances recommendation systems with emotional intelligence  
- 🛒 **Smart Shopping Experience**: Helps users discover products that match their mood instantly  
- 💼 **Business Value**: Boosts engagement, satisfaction, and conversion rates  
- 🌱 **Mental Wellness Impact**: Suggests comforting products when users feel sad or anxious  
- ⚙️ **Future-Ready Approach**: Blends psychology with machine learning for next-gen personalization  

This project represents the **future of emotion-aware computing**, where technology adapts to people — not the other way around.

---

## 🌟 Features

- 🤖 **Real-time Emotion Detection** using DeepFace AI  
- 🛍️ **Smart Product Recommendations** (56+ products mapped to 7 emotions)  
- 🧩 **Category Filtering** (Fashion, Electronics, Wellness, etc.)  
- 💅 **Modern & Responsive UI** built with Tailwind CSS  
- ✨ **Smooth Animations** for enhanced UX  
- 🧠 **Emotion Tracking** within the session  

---

## 😊 Supported Emotions

| Emotion | Recommended Categories |
|----------|------------------------|
| 😊 **Happy** | Entertainment, Fashion, Sports, Electronics |
| 😢 **Sad** | Wellness, Comfort, Self-care, Books, Home |
| 😠 **Angry** | Stress-relief, Wellness, Meditation |
| 😐 **Neutral** | Everyday, Productivity, General, Electronics |
| 😲 **Surprise** | Unique, Gadgets, Mystery, Entertainment |
| 😨 **Fear** | Comfort, Security, Relaxation, Wellness |
| 🤢 **Disgust** | Cleaning, Fresh, Wellness, Home |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | React.js, Tailwind CSS, Axios |
| **Backend** | Flask (Python) |
| **Database** | MongoDB |
| **AI/ML** | DeepFace (Emotion Detection) |
| **Deployment** | Local / Docker Ready |

---

## 📋 Prerequisites

- 🐍 Python 3.8+  
- 🧩 Node.js 14+  
- 🍃 MongoDB (Local or Atlas)  
- 🎥 Webcam  

---

## 🚀 Installation

### 🧠 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
python app.py
Backend runs at 👉 http://localhost:5000

💻 Frontend Setup
bash
Copy code
cd frontend
npm install
npm start
Frontend runs at 👉 http://localhost:3000

🗄️ Database Setup
bash
Copy code
mongosh
cd backend
python seed_products.py
💻 Usage
Open the app → http://localhost:3000

Allow webcam access

Click "🎯 Capture & Analyze"

Look at the camera in good lighting

View your detected emotion 🧠

Explore personalized product recommendations 🛍️

📁 Project Structure
csharp
Copy code
emotion-recommender-app/
├── backend/
│   ├── app.py               # Flask backend
│   ├── seed_products.py     # Database seeding
│   ├── config.py            # Configuration
│   ├── requirements.txt     # Python dependencies
│   └── venv/                # Virtual environment
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── node_modules/
│
└── README.md
🔌 API Endpoints
Endpoint	Method	Description
/api/detect-emotion-simple	POST	Detect emotion from image
/api/categories	GET	Get product categories
/api/health	GET	Health check

🎨 UI Components
📸 Webcam Preview

😀 Emotion Display (emoji + confidence level)

🛒 Product Grid

🔍 Category Filter

📱 Responsive Layout

⚙️ Configuration
backend/config.py
python
Copy code
MONGO_URI = 'mongodb://localhost:27017/emotion_recommender'
DEBUG = True
.env
ini
Copy code
MONGO_URI=mongodb://localhost:27017/emotion_recommender
FLASK_ENV=development
📊 Database Schema
🧑 Users
json
Copy code
{
  "_id": ObjectId,
  "email": "user@example.com",
  "name": "User Name",
  "created_at": ISODate
}
🛍️ Products
json
Copy code
{
  "_id": ObjectId,
  "name": "Product Name",
  "price": "$99.99",
  "category": "Electronics",
  "emotion": "happy",
  "image": "url",
  "description": "Product details"
}
🎯 How It Works
Capture: User captures image via webcam

Analyze: DeepFace detects facial emotion

Detect: System identifies dominant emotion

Match: MongoDB queried for related products

Display: Frontend renders recommendations

🚀 Deployment
Frontend (Vercel)
bash
Copy code
npm install -g vercel
vercel
Backend (Render / Railway)
Push code to GitHub

Connect to Render/Railway

Add environment variables

Deploy

Database (MongoDB Atlas)
Create free cluster

Update MONGO_URI

Re-deploy backend

🐛 Troubleshooting
Issue	Solution
❌ Face not detected	Ensure good lighting & clear face
⚠️ CORS error	Check backend CORS settings for localhost:3000
💾 MongoDB connection failed	Ensure MongoDB is running or Atlas URI is correct
🔒 Port 5000/3000 in use	Kill process or change port

📈 Performance
⚡ Emotion detection: ~1-2 sec

🔍 Query speed: <100ms

🌐 Page load: <2 sec

🧩 Indexed database for performance

🔒 Security
✅ CORS configured

✅ Input validation

✅ MongoDB injection protection

✅ Safe image handling

📚 Resources
DeepFace Documentation

Flask Docs

React Docs

MongoDB Docs

Tailwind CSS

🤝 Contributing
Fork the repo

Create a new branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

🧩 Future Enhancements
 User Authentication

 Shopping Cart & Checkout

 Stripe Payment Integration

 Reviews & Ratings

 Wishlist Feature

 Order History

 Real-time Video Analysis

 Multi-face Detection

 Mobile App Version


