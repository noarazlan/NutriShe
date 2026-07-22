import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../styles/favoritesPopup.css";

function FavoritesPopup({ onClose }) {
  const [favorites, setFavorites] = useState([]);
  const [loading, setLoading] = useState(true);
  const [removingId, setRemovingId] = useState(null);
  const [error, setError] = useState("");

  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    async function fetchFavorites() {
      try {
        setLoading(true);

        const response = await axios.get(
          "http://127.0.0.1:8000/favorites/",
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        console.log("Favorites:", response.data);

        setFavorites(response.data);
        setError("");
      } catch (error) {
        console.error("Could not load favorites:", error.response?.data);
        setError("Could not load favorites.");
      } finally {
        setLoading(false);
      }
    }

    fetchFavorites();
  }, [token]);

  async function removeFavorite(recipeId) {
    try {
      setRemovingId(recipeId);

      const response = await axios.delete(
        `http://127.0.0.1:8000/favorites/remove-from-favorites/${recipeId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      console.log("Removed favorite:", response.data);

      setFavorites((previousFavorites) =>
        previousFavorites.filter((recipe) => recipe.id !== recipeId)
      );
    } catch (error) {
      console.error("Remove failed:", error);
      console.error("Status:", error.response?.status);
      console.error("Response:", error.response?.data);

      setError(
        error.response?.data?.detail || "Could not remove recipe from favorites."
      );
    } finally {
      setRemovingId(null);
    }
  }

  function openRecipe(recipeId) {
    onClose();
    navigate(`/recipes/${recipeId}`);
  }

  return (
    <div className="favorites-overlay" onClick={onClose}>
      <div
        className="favorites-popup"
        onClick={(event) => event.stopPropagation()}
      >
        <div className="favorites-header">
          <h2>Favorite Recipes</h2>

          <button
            type="button"
            className="favorites-close-button"
            onClick={onClose}
          >
            ×
          </button>
        </div>

        <div className="favorites-content">
          {loading && <p className="favorites-message">Loading...</p>}

          {error && <p className="favorites-error">{error}</p>}

          {!loading && !error && favorites.length === 0 && (
            <p className="favorites-message">
              You do not have favorite recipes yet.
            </p>
          )}

          {!loading &&
            favorites.map((recipe) => (
              <article key={recipe.id} className="favorite-item">
                <button
                  type="button"
                  className="favorite-recipe-link"
                  onClick={() => openRecipe(recipe.id)}
                >
                  <img
                    className="favorite-item-image"
                    src={
                      recipe.image_url ||
                      "/images/recipes/default-recipe.jpg"
                    }
                    alt={recipe.name}
                  />

                  <div className="favorite-item-content">
                    <h3>{recipe.name}</h3>

                    {recipe.description && (
                      <p>{recipe.description}</p>
                    )}
                  </div>
                </button>

                <button
                  type="button"
                  className="favorite-remove-button"
                  onClick={() => removeFavorite(recipe.id)}
                  disabled={removingId === recipe.id}
                  aria-label={`Remove ${recipe.name} from favorites`}
                  title="Remove from favorites"
                >
                  {removingId === recipe.id ? "..." : "Remove"}
                </button>
              </article>
            ))}
        </div>
      </div>
    </div>
  );
}

export default FavoritesPopup;