import React from 'react';
import ProductCard from './ProductCard';

const ProductGrid = ({ products, detectedEmotion, selectedCategory }) => {
  if (products.length > 0) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {products.map((product, idx) => (
          <ProductCard key={product.id || idx} product={product} />
        ))}
      </div>
    );
  }

  if (detectedEmotion) {
    return (
      <div className="text-center py-12">
        <p className="text-2xl text-gray-400">😅</p>
        <p className="text-gray-500 text-lg">
          No products found for the selected category. Try another category.
        </p>
      </div>
    );
  }

  return (
    <div className="text-center py-16">
      <p className="text-4xl mb-4">👈</p>
      <p className="text-gray-500 text-lg font-semibold">
        Capture your emotion to see personalized recommendations
      </p>
    </div>
  );
};

export default ProductGrid;
