import React, { useState, useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import '../styles/register.css';

const Register = () => {
  const { register } = useContext(AuthContext);
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    full_name: "",
    username: "",
    email: "",
    password: "",
    date_of_birth: "",
    weight_kg: "",
    height_cm: "",
    activity_level: "none",
    goal: "health",
    life_stage: "standard",
  });

  const [selectedPreferences, setSelectedPreferences] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const preferencesList = [
    { id: 1, name: "Vegetarian" },
    { id: 2, name: "Vegan" },
    { id: 3, name: "Gluten Free" },
    { id: 4, name: "Lactose Free" },
    { id: 5, name: "PCOS" },
  ];

  const handleInputChange = (event) => {
    const { name, value } = event.target;

    setFormData((previousData) => ({
      ...previousData,
      [name]: value,
    }));
  };

  const handlePreferenceChange = (preferenceId) => {
    setSelectedPreferences((previousPreferences) => {
      if (previousPreferences.includes(preferenceId)) {
        return previousPreferences.filter(
          (id) => id !== preferenceId
        );
      }

      return [...previousPreferences, preferenceId];
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setLoading(true);

    const payload = {
      ...formData,
      weight_kg: Number(formData.weight_kg),
      height_cm: Number(formData.height_cm),
      preference_ids: selectedPreferences,
    };

    console.log("Registration payload:", payload);

    try {
      await register(payload);

      navigate("/login");
    } catch (err) {
      console.log("Full registration error:", err);
      console.log("Error response:", err.response);
      console.log("Backend status:", err.response?.status);
      console.log("Backend data:", err.response?.data);

      const detail = err.response?.data?.detail;

      if (Array.isArray(detail)) {
        const errorMessages = detail.map((item) => {
          const fieldName = item.loc?.at(-1) || "field";
          return `${fieldName}: ${item.msg}`;
        });

        setError(errorMessages.join(", "));
      } else if (typeof detail === "string") {
        setError(detail);
      } else if (err.message) {
        setError(err.message);
      } else {
        setError("Registration failed. Try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <div className="form-box register-box">
        <h2>Create Account</h2>

        <p className="subtitle">
          Let's set up your personalized profile
        </p>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <div className="input-group">
              <label htmlFor="full_name">
                Full Name
              </label>

              <input
                id="full_name"
                type="text"
                name="full_name"
                value={formData.full_name}
                onChange={handleInputChange}
                placeholder="Noa Cohen"
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="username">
                Username
              </label>

              <input
                id="username"
                type="text"
                name="username"
                value={formData.username}
                onChange={handleInputChange}
                placeholder="noa_dev"
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="email">
                Email Address
              </label>

              <input
                id="email"
                type="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                placeholder="noa@gmail.com"
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="password">
                Password
              </label>

              <input
                id="password"
                type="password"
                name="password"
                value={formData.password}
                onChange={handleInputChange}
                placeholder="Min 6 characters"
                minLength={6}
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="date_of_birth">
                Date of Birth
              </label>

              <input
                id="date_of_birth"
                type="date"
                name="date_of_birth"
                value={formData.date_of_birth}
                onChange={handleInputChange}
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="weight_kg">
                Weight (kg)
              </label>

              <input
                id="weight_kg"
                type="number"
                name="weight_kg"
                value={formData.weight_kg}
                onChange={handleInputChange}
                placeholder="e.g. 62.5"
                min="30"
                max="300"
                step="0.1"
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="height_cm">
                Height (cm)
              </label>

              <input
                id="height_cm"
                type="number"
                name="height_cm"
                value={formData.height_cm}
                onChange={handleInputChange}
                placeholder="e.g. 165"
                min="100"
                max="250"
                step="0.1"
                required
              />
            </div>

            <div className="input-group">
              <label htmlFor="activity_level">
                Activity Level
              </label>

              <select
                id="activity_level"
                name="activity_level"
                value={formData.activity_level}
                onChange={handleInputChange}
              >
                <option value="none">
                  Sedentary (No training)
                </option>

                <option value="light">
                  Light Activity
                </option>

                <option value="moderate">
                  Moderate Activity
                </option>

                <option value="high">
                  High Activity
                </option>
              </select>
            </div>

            <div className="input-group">
              <label htmlFor="goal">
                Your Goal
              </label>

              <select
                id="goal"
                name="goal"
                value={formData.goal}
                onChange={handleInputChange}
              >
                <option value="health">
                  Overall Health
                </option>

                <option value="maintain">
                  Maintain Weight
                </option>

                <option value="cut">
                  Cut (Weight Loss)
                </option>

                <option value="bulk">
                  Bulk (Muscle Gain)
                </option>
              </select>
            </div>

            <div className="input-group">
              <label htmlFor="life_stage">
                Life Stage
              </label>

              <select
                id="life_stage"
                name="life_stage"
                value={formData.life_stage}
                onChange={handleInputChange}
              >
                <option value="standard">
                  Standard
                </option>

                <option value="pregnancy">
                  Pregnancy
                </option>

                <option value="breastfeeding">
                  Breastfeeding
                </option>
              </select>
            </div>
          </div>

          <div className="preferences-section">
            <span className="section-label">
              Dietary & Health Preferences
            </span>

            <div className="preferences-grid">
              {preferencesList.map((preference) => (
                <label
                  key={preference.id}
                  className="preference-checkbox"
                >
                  <input
                    type="checkbox"
                    checked={selectedPreferences.includes(
                      preference.id
                    )}
                    onChange={() =>
                      handlePreferenceChange(preference.id)
                    }
                  />

                  <span>{preference.name}</span>
                </label>
              ))}
            </div>
          </div>

          <button
            type="submit"
            className="submit-btn"
            disabled={loading}
          >
            {loading
              ? "Creating Account..."
              : "Register"}
          </button>
        </form>

        <p className="redirect-text">
          Already have an account?{" "}
          <Link to="/login">
            Sign In
          </Link>
        </p>
      </div>
    </div>
  );
};

export default Register;