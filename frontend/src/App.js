import React, { useRef, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:5000/api';

function App() {
  const webcamRef = useRef(null);
  const [capturedImage, setCapturedImage] = useState(null);
  const [detectedEmotion, setDetectedEmotion] = useState(null);
  const [emotionConfidence, setEmotionConfidence] = useState(null);
  const [products, setProducts] = useState([]);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [categories, setCategories] = useState(['All']);
  const [error, setError] = useState(null);

  const emotionEmojis = {
    happy: '😊', sad: '😢', angry: '😠', neutral: '😐',
    surprise: '😲', fear: '😨', disgust: '🤢'
  };

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await axios.get(`${API_URL}/categories`);
      setCategories(response.data.categories || ['All']);
    } catch (err) {
      console.error('Error:', err);
    }
  };

  const captureImage = () => {
    if (!webcamRef.current) {
      setError('Webcam not ready');
      return;
    }
    const imageSrc = webcamRef.current.getScreenshot();
    if (!imageSrc) {
      setError('Failed to capture');
      return;
    }
    setCapturedImage(imageSrc);
    analyzeEmotion(imageSrc);
  };

  const analyzeEmotion = async (base64Image) => {
    try {
      setIsAnalyzing(true);
      setError(null);
      
      const response = await axios.post(`${API_URL}/detect-emotion`, {
        image: base64Image
      });

      setDetectedEmotion(response.data.emotion);
      setEmotionConfidence(response.data.confidence);
      setProducts(response.data.products || []);
      setSelectedCategory('All');
      setIsAnalyzing(false);
    } catch (err) {
      console.error('Error:', err);
      setError('Failed to analyze emotion');
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-500 via-purple-500 to-pink-500 p-4">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold text-white text-center mb-8">🎭 Emotion Recommender</h1>

        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6 max-w-4xl mx-auto">
            {error}
          </div>
        )}

        <div className="grid md:grid-cols-3 gap-6">
          {/* Webcam Section */}
          <div className="md:col-span-1">
            <div className="bg-white rounded-lg shadow-xl p-6">
              <h2 className="text-2xl font-bold mb-4">📷 Capture</h2>

              {!detectedEmotion ? (
                <>
                  <div className="bg-black rounded-lg overflow-hidden mb-4">
                    <Webcam ref={webcamRef} screenshotFormat="image/jpeg" className="w-full" />
                  </div>
                  <button
                    onClick={captureImage}
                    disabled={isAnalyzing}
                    className="w-full py-3 bg-blue-600 text-white rounded-lg font-bold hover:bg-blue-700 disabled:opacity-50"
                  >
                    {isAnalyzing ? '⏳ Analyzing...' : '🎯 Capture & Analyze'}
                  </button>
                </>
              ) : (
                <>
                  <img src={capturedImage} alt="Captured" className="w-full rounded-lg mb-4" />
                  <div className="text-center mb-4 p-4 bg-blue-50 rounded">
                    <div className="text-6xl mb-2">{emotionEmojis[detectedEmotion]}</div>
                    <p className="text-2xl font-bold capitalize">{detectedEmotion}</p>
                    <p className="text-lg text-blue-600">{(emotionConfidence * 100).toFixed(0)}%</p>
                  </div>
                  <button
                    onClick={() => {
                      setDetectedEmotion(null);
                      setCapturedImage(null);
                      setProducts([]);
                    }}
                    className="w-full py-3 bg-purple-600 text-white rounded-lg font-bold"
                  >
                    🔄 Detect Again
                  </button>
                </>
              )}
            </div>
          </div>

          {/* Products Section */}
          <div className="md:col-span-2">
            <div className="bg-white rounded-lg shadow-xl p-6">
              <h2 className="text-3xl font-bold mb-6">🛍️ Products</h2>

              {detectedEmotion && (
                <div className="mb-6 flex flex-wrap gap-2">
                  {categories.map((cat) => (
                    <button
                      key={cat}
                      onClick={() => setSelectedCategory(cat)}
                      className={`px-4 py-2 rounded font-bold ${
                        selectedCategory === cat
                          ? 'bg-blue-600 text-white'
                          : 'bg-gray-200 text-gray-800'
                      }`}
                    >
                      {cat}
                    </button>
                  ))}
                </div>
              )}

              {products && products.length > 0 ? (
                <div className="grid md:grid-cols-2 gap-4">
                  {products
                    .filter(p => selectedCategory === 'All' || p.category === selectedCategory)
                    .map((product) => (
                      <div key={product.id} className="bg-gray-50 rounded-lg overflow-hidden shadow">
                        <img
                          src={product.image}
                          alt={product.name}
                          className="w-full h-40 object-cover"
                          onError={(e) => {
                            e.target.src = 'https://via.placeholder.com/300?text=Product';
                          }}
                        />
                        <div className="p-4">
                          <h3 className="font-bold text-gray-800 mb-2 line-clamp-2">{product.name}</h3>
                          <div className="flex justify-between items-center">
                            <span className="text-2xl font-bold text-blue-600">${product.price}</span>
                            <span className="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">
                              {product.category}
                            </span>
                          </div>
                          <button className="w-full mt-3 py-2 bg-blue-600 text-white rounded font-bold hover:bg-blue-700">
                            🛒 Add to Cart
                          </button>
                        </div>
                      </div>
                    ))}
                </div>
              ) : detectedEmotion ? (
                <p className="text-gray-500 text-center py-8">No products found</p>
              ) : (
                <p className="text-gray-500 text-center py-8">Capture emotion to see products</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
