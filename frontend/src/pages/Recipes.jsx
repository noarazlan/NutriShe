import { useEffect, useState } from "react";
import axios from "axios";
import RecipeCard from "../components/RecipeCard";

function Recipes() {
  const [recipes, setRecipes] = useState([]);
  const [favoriteIds, setFavoriteIds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchData() {
      try {
        const token = localStorage.getItem("token");

        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };

        const [recipesResponse, favoritesResponse] = await Promise.all([
          axios.get("http://127.0.0.1:8000/recipes/", config),
          axios.get("http://127.0.0.1:8000/favorites/", config),
        ]);

        setRecipes(recipesResponse.data);

        setFavoriteIds(
          favoritesResponse.data.map((recipe) => recipe.id)
        );
      } catch (err) {
        console.error("Recipes page error:", err);
        setError(
          err.response?.data?.detail || "Could not load recipes."
        );
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) {
    return <p>Loading recipes...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <main className="recipes-page">
      <h1>Recipes</h1>

      {recipes.length === 0 ? (
        <p>No recipes were found.</p>
      ) : (
        <div className="recipes-container">
          {recipes.map((recipe) => (
            <RecipeCard
              key={recipe.id}
              recipe={{
                ...recipe,
                is_favorite: favoriteIds.includes(recipe.id),
              }}
            />
          ))}
        </div>
      )}
    </main>
  );
}

export default Recipes;