import React from "react";
import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import ProtectedRoute from "./components/ProtectedRoute";

// Importing Pages
import Login from "./pages/Login";
import Register from "./pages/Register";
import Protein from "./pages/Protein";
import Fiber from "./pages/Fiber";
import Fats from "./pages/Fats";
import Carbohydrates from "./pages/Carbohydrates";

// Temporary Home Component
const TempHome = () => {
  return (
    <div style={{ padding: "40px", textAlign: "center", fontFamily: "sans-serif" }}>
      <h1>🎉 NutriShe Dashboard</h1>
      <p>Welcome! Navigation paths are active. Navigate manually or click below:</p>
      <div style={{ marginTop: "20px", display: "flex", justifyContent: "center", gap: "10px" }}>
        <a href="/protein">Protein</a> | 
        <a href="/fiber">Fiber</a> | 
        <a href="/fats">Fats</a> | 
        <a href="/carbohydrates">Carbohydrates</a>
      </div>
    </div>
  );
};

// Modern routing setup matching your createBrowserRouter preference
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
    path: "/protein",
    element: (
      <ProtectedRoute>
        <Protein />
      </ProtectedRoute>
    ),
  },
  {
    path: "/fiber",
    element: (
      <ProtectedRoute>
        <Fiber />
      </ProtectedRoute>
    ),
  },
  {
    path: "/fats",
    element: (
      <ProtectedRoute>
        <Fats />
      </ProtectedRoute>
    ),
  },
  {
    path: "/carbohydrates",
    element: (
      <ProtectedRoute>
        <Carbohydrates />
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
