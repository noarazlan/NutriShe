import { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

function RecipeCard({ recipe }) {
  const [isFavorite, setIsFavorite] = useState(recipe.is_favorite);
  const [isLoading, setIsLoading] = useState(false);

  async function handleFavoriteClick(event) {
    event.preventDefault();
    event.stopPropagation();

    if (isLoading) {
      return;
    }

    const token = localStorage.getItem("token");

    if (!token) {
      console.error("No token was found.");
      return;
    }

    try {
      setIsLoading(true);

      if (isFavorite) {
        await axios.delete(
          `http://127.0.0.1:8000/favorites/remove-from-favorites/${recipe.id}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        setIsFavorite(false);
      } else {
        await axios.post(
          `http://127.0.0.1:8000/favorites/${recipe.id}`,
          {},
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        setIsFavorite(true);
      }
    } catch (error) {
      console.error("Favorite request failed:", error);
      console.error("Status:", error.response?.status);
      console.error("Response:", error.response?.data);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <article className="recipe-card">
      <button
        type="button"
        className="favorite-btn"
        onClick={handleFavoriteClick}
        disabled={isLoading}
        aria-label={
          isFavorite
            ? `Remove ${recipe.name} from favorites`
            : `Add ${recipe.name} to favorites`
        }
      >
        {isFavorite ? "♥" : "♡"}
      </button>

      <Link to={`/recipes/${recipe.id}`} className="recipe-card-link">
        <div className="recipe-image-wrapper">
          <img
            className="recipe-image"
            src={recipe.image_url}
            alt={recipe.name}
          />
        </div>

        <div className="recipe-card-content">
          <h3 className="recipe-card-title">{recipe.name}</h3>

          {recipe.description && (
            <p className="recipe-card-description">{recipe.description}</p>
          )}

          <div className="recipe-card-meta">
            {recipe.preparation_time_minutes != null && (
              <span>{recipe.preparation_time_minutes} min</span>
            )}

            {recipe.servings != null && (
              <span>{recipe.servings} servings</span>
            )}
          </div>
        </div>
      </Link>
    </article>
  );
}

export default RecipeCard;