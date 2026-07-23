import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../styles/home.css"; 
import RecipeCard from "../components/RecipeCard";
import HomeTips from "../components/HomeTips";

const HomePage = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [recipes, setRecipes] = useState([]);
  const [showMicronutrients, setShowMicronutrients] = useState(false);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
            setError("You must log in first");
            return;}

        const headers = {Authorization: `Bearer ${token}`,};
        const [targetResponse, recipesResponse] = await Promise.all([
          axios.get("http://localhost:8000/target/me", {headers}),
          axios.get("http://localhost:8000/recipes/", {headers}), ]);

        
        setData(targetResponse.data);
        const shuffledRecipes = [...recipesResponse.data].sort(
        () => Math.random() - 0.5
        );

        setRecipes(shuffledRecipes.slice(0, 4));

      } catch (error) {
        console.log("Error:", error);
        setError(
          error.response?.data?.detail || "Could not load your dashboard"
        );
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="loading-box">Loading your personalized dashboard...</div>;
  }

  if (error) {
    return <div className="error-box">{error}</div>;
  }

  if (!data) {
    return <div className="error-box">No target data was found.</div>;
  }

  return (
    <div className="home-container">
      {/* Header section */}
      <header className="home-header">
        <h1>Hello {data.full_name || "User"},</h1>
            <h1> welcome to your fitness journey</h1>
        <h2>Here are your goals for today</h2>
      </header>

      {/* Macronutrient Cards Navigation */}
      <div className="macro-grid">
        <Link to="/protein" className="macro-card">
          <span className="macro-title">Protein</span>
          <span className="macro-value">
            {data.protein_target_g ?? data.protein ?? 0} <span className="macro-unit">g</span>
          </span>
        </Link>

        <Link to="/fats" className="macro-card">
          <span className="macro-title">Fats</span>
          <span className="macro-value">
            {data.fat_target_g ?? data.fat ?? 0} <span className="macro-unit">g</span>
          </span>
        </Link>

        <Link to="/carbohydrates" className="macro-card">
          <span className="macro-title">Carbohydrates</span>
          <span className="macro-value">
            {data.carbohydrates_target_g ?? data.carbohydrates ?? 0} <span className="macro-unit">g</span>
          </span>
        </Link>

        <Link to="/fiber" className="macro-card">
          <span className="macro-title">Fiber</span>
          <span className="macro-value">
            {data.fiber_target_g ?? data.fiber ?? 0} <span className="macro-unit">g</span>
          </span>
        </Link>
      </div>

      {/* Micronutrients Section */}
      <section className="micro-section">
        <button
          type="button"
          className="toggle-micro-btn"
          onClick={() => setShowMicronutrients((prev) => !prev)}
          aria-expanded={showMicronutrients}
        >
          {showMicronutrients
            ? "▲ Hide vitamins & minerals"
            : "▼ View vitamins & minerals"}
        </button>

        {showMicronutrients && (
          <div className="micro-grid">
            <div className="micro-item">
              <span className="micro-name">Iron</span>
              <span className="micro-value">{data.iron_target_mg ?? data.iron ?? 0} mg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Calcium</span>
              <span className="micro-value">{data.calcium_target_mg ?? data.calcium ?? 0} mg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Magnesium</span>
              <span className="micro-value">{data.magnesium_target_mg ?? data.magnesium ?? 0} mg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Potassium</span>
              <span className="micro-value">{data.potassium_target_mg ?? data.potassium ?? 0} mg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Sodium</span>
              <span className="micro-value">{data.sodium_target_mg ?? data.sodium ?? 0} mg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Vitamin A</span>
              <span className="micro-value">{data.vitamin_a_target_mcg ?? data.vitamin_a ?? 0} mcg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Vitamin C</span>
              <span className="micro-value">{data.vitamin_c_target_mg ?? data.vitamin_c ?? 0} mg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Vitamin D</span>
              <span className="micro-value">{data.vitamin_d_target_mcg ?? data.vitamin_d ?? 0} mcg</span>
            </div>
            <div className="micro-item">
              <span className="micro-name">Vitamin B12</span>
              <span className="micro-value">{data.vitamin_b12_target_mcg ?? data.vitamin_b12 ?? 0} mcg</span>
            </div>
          </div>
        )}
      </section>

      <section className="recommendations-section">
          <h2>Today's recommendations</h2>

          {recipes.length === 0 ? (<p>No matching recipes were found.</p>) : (
            <div className="recipes-container">
                {recipes.map((recipe) => (
                    <RecipeCard key={recipe.id} recipe={recipe} />
                ))}
            </div>
          )}
        </section>
        <HomeTips />
    </div>
  );
};

export default HomePage;