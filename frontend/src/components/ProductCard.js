import React from 'react';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card bg-gray-50 rounded-lg overflow-hidden shadow hover:shadow-lg transition">
      <div className="relative h-48 bg-gray-200 overflow-hidden">
        <img
          src={product.image}
          alt={product.name}
          className="w-full h-full object-cover hover:scale-110 transition-transform duration-300"
          onError={(e) => {
            e.target.src = 'https://via.placeholder.com/400x300?text=Product+Image';
          }}
        />
      </div>
      <div className="p-4">
        <h3 className="font-bold text-gray-800 mb-2 line-clamp-2">
          {product.name}
        </h3>
        <div className="flex justify-between items-start gap-2 mb-3">
          <span className="text-2xl font-bold text-blue-600">{product.price}</span>
          <span className="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded-full whitespace-nowrap">
            {product.category}
          </span>
        </div>
        <button className="w-full py-2 bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-lg font-semibold hover:from-blue-600 hover:to-purple-600 transition">
          Add to Cart
        </button>
      </div>
    </div>
  );
};

export default ProductCard;
