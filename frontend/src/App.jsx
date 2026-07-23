import React from "react";
import {
  createBrowserRouter,
  RouterProvider,
  Navigate,
} from "react-router-dom";

import { AuthProvider } from "./context/AuthContext";
import ProtectedRoute from "./components/ProtectedRoute";
import MainLayout from "./layouts/MainLayout";


// Importing Pages
import Login from "./pages/Login";
import Register from "./pages/Register";
import Protein from "./pages/Protein";
import Fiber from "./pages/Fiber";
import Fats from "./pages/Fats";
import Carbohydrates from "./pages/Carbohydrates";
import HomePage from "./pages/Home";
import RecipesPage from "./pages/Recipes";
import RecipeDetailsPage from "./pages/RecipeDetails";
import TipsPage from "./pages/Tips";

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
    element: (
      <ProtectedRoute>
        <MainLayout />
      </ProtectedRoute>
    ),

    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "/protein",
        element: <Protein />,
      },
      {
        path: "/fiber",
        element: <Fiber />,
      },
      {
        path: "/fats",
        element: <Fats />,
      },
      {
        path: "/carbohydrates",
        element: <Carbohydrates />,
      },
      {
        path: "/recipes",
        element: <RecipesPage />,
      },
      {
         path: "/recipes/:id",
        element: <RecipeDetailsPage />,
      },
      {
        path: "/tips",
        element: <TipsPage />,
      },
    ],
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