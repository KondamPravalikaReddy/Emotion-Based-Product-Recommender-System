import React from 'react';

const CategoryFilter = ({ categories, selectedCategory, onCategoryChange }) => {
  return (
    <div className="mb-6 p-4 bg-gray-50 rounded-lg">
      <label className="block text-sm font-bold text-gray-700 mb-3">
        🏷️ Filter by Category:
      </label>
      <div className="flex flex-wrap gap-2">
        {categories.map((category) => (
          <button
            key={category}
            onClick={() => onCategoryChange(category)}
            className={`px-4 py-2 rounded-full font-semibold transition ${
              selectedCategory === category
                ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg'
                : 'bg-white text-gray-800 border border-gray-300 hover:border-blue-500'
            }`}
          >
            {category}
          </button>
        ))}
      </div>
    </div>
  );
};

export default CategoryFilter;
