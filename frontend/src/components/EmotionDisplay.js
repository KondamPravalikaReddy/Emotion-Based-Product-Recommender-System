import React from 'react';

const EmotionDisplay = ({ emotion, confidence, emotionEmojis }) => {
  if (!emotion) return null;

  return (
    <div className="text-center p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg mb-4 fade-in">
      <div className="text-6xl mb-2">{emotionEmojis[emotion] || '😐'}</div>
      <p className="text-3xl font-bold text-gray-800 capitalize mb-2">{emotion}</p>
      <div className="flex justify-center items-center gap-2">
        <div className="w-32 bg-gray-200 rounded-full h-2">
          <div
            className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full"
            style={{ width: `${confidence * 100}%` }}
          ></div>
        </div>
        <span className="text-sm font-bold text-gray-700">
          {(confidence * 100).toFixed(0)}%
        </span>
      </div>
    </div>
  );
};

export default EmotionDisplay;
