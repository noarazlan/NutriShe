import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../styles/recipeDetailsPage.css";

function RecipeDetailsPage() {
  const { id } = useParams();

  const [recipe, setRecipe] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchRecipe() {
      try {
        setLoading(true);
        setError("");

        const token = localStorage.getItem("token");

        const response = await axios.get(
          `http://127.0.0.1:8000/recipes/${id}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        console.log("Recipe details:", response.data);

        setRecipe(response.data);
      } catch (error) {
        console.error(error);
        console.error(error.response?.status);
        console.error(error.response?.data);

        setError("Could not load the recipe.");
        
      } finally {
        setLoading(false);
      }
    }

    fetchRecipe();
  }, [id]);

  if (loading) {
    return <p className="recipe-details-message">Loading recipe...</p>;
  }

  if (error) {
    return <p className="recipe-details-error">{error}</p>;
  }

  if (!recipe) {
    return <p className="recipe-details-message">Recipe not found.</p>;
  }

 return (
  <main className="recipe-details-page">
    <div className="recipe-details-card">
      <img
        className="recipe-details-image"
        src={recipe.image_url}
        alt={recipe.name}
      />

      <div className="recipe-details-content">
        <h1>{recipe.name}</h1>

        <p className="recipe-description">
          {recipe.description}
        </p>

        <div className="recipe-info">
          <div className="recipe-info-box">
            <span className="recipe-info-title">⏱ Preparation</span>
            <span>{recipe.preparation_time_minutes} min</span>
          </div>

          <div className="recipe-info-box">
            <span className="recipe-info-title">🍽 Servings</span>
            <span>{recipe.servings}</span>
          </div>
        </div>

        {recipe.meal_types.length > 0 && (
          <>
            <h2>Meal Type</h2>

            <div className="recipe-tags">
              {recipe.meal_types.map((meal) => (
                <span
                  key={meal.meal_type}
                  className="recipe-tag"
                >
                  {meal.meal_type}
                </span>
              ))}
            </div>
          </>
        )}

        {recipe.preferences.length > 0 && (
          <>
            <h2>Suitable For</h2>

            <div className="recipe-tags">
              {recipe.preferences.map((pref) => (
                <span
                  key={pref.preference.code}
                  className="recipe-tag"
                >
                  {pref.preference.display_name}
                </span>
              ))}
            </div>
          </>
        )}

        <h2>Ingredients</h2>

        <div className="recipe-section">
          {recipe.ingredients_text}
        </div>

        <h2>Instructions</h2>

        <div className="recipe-section">
          {recipe.instructions}
        </div>
      </div>
    </div>
  </main>
);
}

export default RecipeDetailsPage;