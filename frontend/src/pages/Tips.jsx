import { useEffect, useState } from "react";
import axios from "axios";
import TipsCard from "../components/TipsCard";
import "../styles/tipsPage.css";

function TipsPage() {
  const [tips, setTips] = useState([]);
  const [showingAllTips, setShowingAllTips] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  async function fetchTips(showAll = false) {
    try {
      setIsLoading(true);
      setError("");

      const token = localStorage.getItem("token");

      if (!token) {
        setError("You must log in first.");
        return;
      }

      const endpoint = showAll
        ? "http://127.0.0.1:8000/tips/all-tips"
        : "http://127.0.0.1:8000/tips";

      const response = await axios.get(endpoint, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setTips(response.data);
      setShowingAllTips(showAll);
    } catch (error) {
      console.error("Failed to load tips:", error);

      setError(
        error.response?.data?.detail ||
          "Could not load the tips."
      );
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    fetchTips(false);
  }, []);

  function handleToggleTips() {
    fetchTips(!showingAllTips);
  }

  return (
    <main className="tips-page">
      <header className="tips-page-header">
        <span className="tips-page-icon">🌸</span>

        <h1>
          {showingAllTips
            ? "All Nutrition Tips"
            : "Tips Selected for You"}
        </h1>

        <p>
          {showingAllTips
            ? "Explore all the nutrition and wellness tips available in NutriShe."
            : "Personalized and general tips chosen according to your preferences."}
        </p>

        <button
          type="button"
          className="tips-toggle-button"
          onClick={handleToggleTips}
          disabled={isLoading}
        >
          {showingAllTips
            ? "Show personalized tips"
            : "View all tips"}
        </button>
      </header>

      {isLoading && (
        <p className="tips-page-message">
          Loading tips...
        </p>
      )}

      {!isLoading && error && (
        <p className="tips-page-message tips-page-error">
          {error}
        </p>
      )}

      {!isLoading && !error && tips.length === 0 && (
        <p className="tips-page-message">
          No tips are available right now.
        </p>
      )}

      {!isLoading && !error && tips.length > 0 && (
        <section className="tips-page-grid">
          {tips.map((tip) => (
            <TipsCard
              key={tip.id}
              tip={tip}
            />
          ))}
        </section>
      )}
    </main>
  );
}

export default TipsPage;