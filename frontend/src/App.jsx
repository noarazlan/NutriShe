import React from "react";
import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import ProtectedRoute from "./components/ProtectedRoute";

// Importing Pages
import Login from "./pages/Login";
import Register from "./pages/Register";
//import Protein from "./pages/Protein";
//import Fiber from "./pages/Fiber";
//import Fats from "./pages/Fats";
//import Carbohydrates from "./pages/Carbohydrates";


// Temporary Home/Dashboard component
const TempHome = () => {
  return (
    <div style={{ padding: "40px", textAlign: "center", fontFamily: "sans-serif" }}>
      <h1>🎉 NutriShe Dashboard</h1>
      <p>Successfully Logged In! Use the navigation below to check nutrients.</p>
    </div>
  );
};

// Creating the modern browser router configuration
const router = createBrowserRouter([
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/register",
    element: <Register />,
  },
  {
    path: "/",
    element: (
      <ProtectedRoute>
        <TempHome />
      </ProtectedRoute>
    ),
  },
  {
    path: "*",
    element: <Navigate to="/" replace />,
  },
]);

function App() {
  return (
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
  );
}

export default App;