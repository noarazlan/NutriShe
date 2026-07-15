import React, { useState, useContext } from "react";
import { useNavigate, Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";


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
  });

  const [selectedPreferences, setSelectedPreferences] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // Available preferences matched to database seed IDs
  const preferencesList = [
    { id: 1, name: "Vegetarian" },
    { id: 2, name: "Vegan" },
    { id: 3, name: "Gluten Free" },
    { id: 4, name: "Lactose Free" },
    { id: 5, name: "PCOS" },
  ];

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handlePreferenceChange = (id) => {
    if (selectedPreferences.includes(id)) {
      setSelectedPreferences(selectedPreferences.filter((pId) => pId !== id));
    } else {
      setSelectedPreferences([...selectedPreferences, id]);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    const payload = {
      ...formData,
      weight_kg: parseFloat(formData.weight_kg),
      height_cm: parseFloat(formData.height_cm),
      preference_ids: selectedPreferences,
    };

    try {
      await register(payload);
      navigate("/login"); // Redirect to login page upon registration
    } catch (err) {
      setError(err.response?.data?.detail || "Registration failed. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <div className="form-box register-box">
        <h2>Create Account</h2>
        <p className="subtitle">Let's set up your personalized profile</p>

        {error && <div className="error-message">{error}</div>}

        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            {/* Personal Details */}
            <div className="input-group">
              <label>Full Name</label>
              <input
                type="text"
                name="full_name"
                value={formData.full_name}
                onChange={handleInputChange}
                placeholder="Noa Cohen"
                required
              />
            </div>

            <div className="input-group">
              <label>Username</label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleInputChange}
                placeholder="noa_dev"
                required
              />
            </div>

            <div className="input-group">
              <label>Email Address</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                placeholder="noa@gmail.com"
                required
              />
            </div>

            <div className="input-group">
              <label>Password</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleInputChange}
                placeholder="Min 6 characters"
                required
              />
            </div>

            <div className="input-group">
              <label>Date of Birth</label>
              <input
                type="date"
                name="date_of_birth"
                value={formData.date_of_birth}
                onChange={handleInputChange}
                required
              />
            </div>

            {/* Metrics */}
            <div className="input-group">
              <label>Weight (kg)</label>
              <input
                type="number"
                step="0.1"
                name="weight_kg"
                value={formData.weight_kg}
                onChange={handleInputChange}
                placeholder="e.g. 62.5"
                required
              />
            </div>

            <div className="input-group">
              <label>Height (cm)</label>
              <input
                type="number"
                step="0.1"
                name="height_cm"
                value={formData.height_cm}
                onChange={handleInputChange}
                placeholder="e.g. 165"
                required
              />
            </div>

            {/* Select Options */}
            <div className="input-group">
              <label>Activity Level</label>
              <select
                name="activity_level"
                value={formData.activity_level}
                onChange={handleInputChange}
              >
                <option value="none">Sedentary (No training)</option>
                <option value="light">Light Activity</option>
                <option value="moderate">Moderate Activity</option>
                <option value="high">High Activity</option>
              </select>
            </div>

            <div className="input-group">
              <label>Your Goal</label>
              <select
                name="goal"
                value={formData.goal}
                onChange={handleInputChange}
              >
                <option value="health">Overall Health</option>
                <option value="maintain">Maintain Weight</option>
                <option value="cut">Cut (Weight Loss)</option>
                <option value="bulk">Bulk (Muscle Gain)</option>
              </select>
            </div>
          </div>

          {/* Diet Preferences Checkboxes */}
          <div className="preferences-section">
            <label className="section-label">Dietary & Health Preferences</label>
            <div className="preferences-grid">
              {preferencesList.map((pref) => (
                <label key={pref.id} className="preference-checkbox">
                  <input
                    type="checkbox"
                    checked={selectedPreferences.includes(pref.id)}
                    onChange={() => handlePreferenceChange(pref.id)}
                  />
                  <span>{pref.name}</span>
                </label>
              ))}
            </div>
          </div>

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Creating Account..." : "Register"}
          </button>
        </form>

        <p className="redirect-text">
          Already have an account? <Link to="/login">Sign In</Link>
        </p>
      </div>
    </div>
  );
};

export default Register;