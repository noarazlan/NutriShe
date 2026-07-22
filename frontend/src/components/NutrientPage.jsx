import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axiosClient from "../api/Client";
import "../styles/nutrient-page.css";

const NutrientPage = ({ title, description, categoryKey, unit }) => {
  const [foods, setFoods] = useState([]);
  const [searchTerm, setSearchTerm] = useState(""); // State for the search input
  const [selectedFoods, setSelectedFoods] = useState([]);
  const [totalNutrient, setTotalNutrient] = useState(0);
  const [dailyReferenceValue, setDailyReferenceValue] = useState(0);
  const [errorMessage, setErrorMessage] = useState("");
  const [customGrams, setCustomGrams] = useState({});

  // Fetch filtered foods AND dynamic nutrient reference values
  useEffect(() => {
    const fetchData = async () => {
      try {
        // 1. Fetch filtered foods based on user's dietary preferences
        const foodsResponse = await axiosClient.get(`/foods/category/${categoryKey}`);
        setFoods(foodsResponse.data);

        // 2. Fetch daily reference target based on user's age
        const refResponse = await axiosClient.get(`/foods/reference/${categoryKey}`);
        setDailyReferenceValue(Number(refResponse.data.recommended_amount));
      } catch (error) {
        setErrorMessage("Failed to load data. Ensure both backend and seeds are initialized.");
        console.error("Error fetching page data:", error);
      }
    };
    fetchData();
  }, [categoryKey]);

  const handleGramChange = (foodId, value) => {
    setCustomGrams({ ...customGrams, [foodId]: value });
  };

  // Add food (used by both drag-and-drop and click)
  const addFoodToPlate = (food, gramsInput) => {
    const grams = parseFloat(gramsInput || "100");
    if (isNaN(grams) || grams <= 0) {
      alert("Please enter a valid amount in grams.");
      return;
    }

    const nutrientField = `${categoryKey}_per_100g`;
    const nutrientValue = (Number(food[nutrientField]) * grams) / 100;

    const newListItem = {
      id: Date.now(),
      name: food.name,
      grams,
      calculatedValue: nutrientValue,
    };

    setSelectedFoods((prev) => [...prev, newListItem]);
    setTotalNutrient((prev) => prev + nutrientValue);
  };

  const handleRemoveFood = (itemToRemove) => {
    setSelectedFoods((prev) => prev.filter((item) => item.id !== itemToRemove.id));
    setTotalNutrient((prev) => prev - itemToRemove.calculatedValue);
  };

  // Drag and Drop Handlers
  const handleDragStart = (e, food) => {
    e.dataTransfer.setData("application/json", JSON.stringify(food));
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    try {
      const foodData = e.dataTransfer.getData("application/json");
      if (!foodData) return;
      
      const food = JSON.parse(foodData);
      const gramsInput = customGrams[food.id] || "100";
      addFoodToPlate(food, gramsInput);
    } catch (err) {
      console.error("Failed to process dropped item:", err);
    }
  };

  // Filter foods locally in real-time based on the search term (case-insensitive)
  const filteredFoods = foods.filter((food) =>
    food.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // Calculate percentage of daily target completed
  const completionPercentage = dailyReferenceValue > 0 
    ? Math.min((totalNutrient / dailyReferenceValue) * 100, 100) 
    : 0;

  return (
    <div className="nutrient-container">
      <header className="nutrient-header">
        <div className="navigation-wrapper">
          <Link to="/" className="back-home-btn">
            ← Back to Dashboard
          </Link>
        </div>

        <h1>{title}</h1>
        <p className="nutrient-description">{description}</p>
        
        {dailyReferenceValue > 0 && (
          <div className="target-progress-box">
            <span className="target-text">Your Recommended Daily Target: <strong>{dailyReferenceValue} {unit}</strong></span>
            <div className="progress-bar-container">
              <div 
                className="progress-bar-fill" 
                style={{ width: `${completionPercentage}%` }}
              ></div>
            </div>
            <span className="percentage-text">{completionPercentage.toFixed(0)}% Completed</span>
          </div>
        )}
      </header>

      {errorMessage && <div className="error-banner">{errorMessage}</div>}

      <div className="nutrient-workspace">
        {/* Food Pool Selection */}
        <div className="foods-pool">
          <h3>Food Database</h3>
          
          {/* Real-time Search Input Box */}
          <div className="search-wrapper">
            <input
              type="text"
              placeholder="🔍 Search food items..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="food-search-input"
            />
          </div>

          <p className="helper-text">Drag any card or enter grams and click 'Add'</p>
          
          <div className="foods-grid">
            {filteredFoods.length === 0 ? (
              <p className="no-results-text">No matching foods found.</p>
            ) : (
              filteredFoods.map((food) => {
                const fieldName = `${categoryKey}_per_100g`;
                const currentInput = customGrams[food.id] || "100";
                
                return (
                  <div 
                    key={food.id} 
                    className="food-card draggable"
                    draggable
                    onDragStart={(e) => handleDragStart(e, food)}
                  >
                    <div className="food-card-info">
                      <h4>{food.name}</h4>
                      <p className="nutrient-value">
                        {Number(food[fieldName]).toFixed(1)}{unit} <span className="light-text">/ 100g</span>
                      </p>
                    </div>
                    
                    <div className="food-card-actions">
                      <div className="gram-input-wrapper">
                        <input
                          type="number"
                          min="1"
                          value={currentInput}
                          onChange={(e) => handleGramChange(food.id, e.target.value)}
                          className="grams-input"
                        />
                        <span className="grams-label">g</span>
                      </div>
                      <button 
                        className="add-to-plate-btn"
                        onClick={() => addFoodToPlate(food, currentInput)}
                      >
                        Add
                      </button>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>

        {/* Drag and Drop Target Plate */}
        <div 
          className="selected-foods-box drop-zone"
          onDragOver={handleDragOver}
          onDrop={handleDrop}
        >
          <h3>My Plate (Drop Foods Here)</h3>
          <div className="selected-list">
            {selectedFoods.length === 0 ? (
              <div className="empty-plate-placeholder">
                <div className="plate-outline"></div>
                <p className="placeholder-text">Drag foods here or click 'Add' to calculate intake!</p>
              </div>
            ) : (
              selectedFoods.map((item) => (
                <div key={item.id} className="selected-item animate-in">
                  <span className="item-details">{item.name} ({item.grams}g)</span>
                  <span className="item-value">+{item.calculatedValue.toFixed(1)}{unit}</span>
                  <button className="remove-btn" onClick={() => handleRemoveFood(item)}>✕</button>
                </div>
              ))
            )}
          </div>
          <div className="total-summary">
            <h4>Total {title}:</h4>
            <span className="total-badge">{totalNutrient.toFixed(1)} {unit}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NutrientPage;