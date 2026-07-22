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
import HomePage from "./pages/Home";



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
        <HomePage />
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
