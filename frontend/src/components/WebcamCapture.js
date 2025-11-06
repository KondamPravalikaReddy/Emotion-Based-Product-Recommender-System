import React from 'react';
import Webcam from 'react-webcam';

const WebcamCapture = ({
  webcamRef,
  capturedImage,
  detectedEmotion,
  emotionConfidence,
  emotionEmojis,
  isAnalyzing,
  onCapture,
  onDetectAgain,
  onWebcamReady
}) => {
  return (
    <div className="bg-white rounded-lg shadow-xl p-6 fade-in">
      <h2 className="text-2xl font-bold mb-4 text-gray-800">📷 Capture Your Emotion</h2>

      {!detectedEmotion ? (
        <>
          <div className="relative bg-black rounded-lg overflow-hidden mb-4">
            <Webcam
              ref={webcamRef}
              screenshotFormat="image/jpeg"
              className="w-full"
              videoConstraints={{
                width: { ideal: 640 },
                height: { ideal: 480 },
                facingMode: 'user'
              }}
              onUserMedia={onWebcamReady}
            />
            <div className="absolute bottom-2 right-2 text-white text-xs bg-black bg-opacity-50 px-2 py-1 rounded">
              📸 Live Preview
            </div>
          </div>

          <button
            onClick={onCapture}
            disabled={isAnalyzing}
            className={`w-full py-3 rounded-lg font-bold text-white text-lg transition ${
              isAnalyzing
                ? 'bg-gray-400 cursor-not-allowed'
                : 'bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 shadow-lg'
            }`}
          >
            {isAnalyzing ? (
              <span className="flex justify-center items-center">
                <span className="spinner mr-2" style={{width: '20px', height: '20px'}}></span>
                Analyzing...
              </span>
            ) : (
              '🎯 Capture & Analyze Emotion'
            )}
          </button>

          <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded text-sm text-gray-700">
            <p className="font-semibold mb-1">💡 Tips:</p>
            <ul className="text-xs space-y-1">
              <li>• Ensure good lighting</li>
              <li>• Face the camera directly</li>
              <li>• Clear facial expression</li>
            </ul>
          </div>
        </>
      ) : (
        <>
          <div className="relative bg-gray-100 rounded-lg overflow-hidden mb-4">
            <img src={capturedImage} alt="Captured" className="w-full" />
          </div>

          <div className="text-center mb-6 p-4 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg">
            <div className="text-7xl mb-2">{emotionEmojis[detectedEmotion] || '😐'}</div>
            <p className="text-3xl font-bold text-gray-800 capitalize mb-2">
              {detectedEmotion}
            </p>
            <div className="flex justify-center items-center gap-2">
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full transition-all"
                  style={{ width: `${emotionConfidence * 100}%` }}
                ></div>
              </div>
              <span className="text-sm font-bold text-gray-700 w-12">
                {(emotionConfidence * 100).toFixed(0)}%
              </span>
            </div>
          </div>

          <button
            onClick={onDetectAgain}
            className="w-full py-3 rounded-lg font-bold text-white bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 transition shadow-lg"
          >
            🔄 Detect Again
          </button>
        </>
      )}
    </div>
  );
};

export default WebcamCapture;
