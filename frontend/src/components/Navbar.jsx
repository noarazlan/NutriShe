import { useEffect, useRef, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import FavoritesPopup from "./FavoritesPopup";
import "../styles/navbar.css";

function Navbar() {
  const navigate = useNavigate();

  const [showFavorites, setShowFavorites] = useState(false);

  const favoritesContainerRef = useRef(null);

  function handleLogout() {
    localStorage.removeItem("token");
    navigate("/login");
  }

  function toggleFavorites() {
    setShowFavorites((prev) => !prev);
  }

  function closeFavorites() {
    setShowFavorites(false);
  }

  useEffect(() => {
    function handleClickOutside(event) {
      if (
        favoritesContainerRef.current &&
        !favoritesContainerRef.current.contains(event.target)
      ) {
        closeFavorites();
      }
    }

    document.addEventListener("mousedown", handleClickOutside);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <Link to="/" className="navbar-brand">
          NutriShe
        </Link>

        <div className="navbar-links">
          <Link to="/">Home</Link>

          <Link to="/recipes">Recipes</Link>


          <button
            type="button"
            className="logout-btn"
            onClick={handleLogout}
          >
            Logout
          </button>
        </div>
      </div>

      <div
        className="favorites-navbar-container"
        ref={favoritesContainerRef}
      >
        <button
          type="button"
          className="favorites-button"
          onClick={toggleFavorites}
          aria-label="Open favorite recipes"
          aria-expanded={showFavorites}
        >
          ♡
        </button>

        {showFavorites && (
          <FavoritesPopup onClose={closeFavorites} />
        )}
      </div>
    </nav>
  );
}

export default Navbar;