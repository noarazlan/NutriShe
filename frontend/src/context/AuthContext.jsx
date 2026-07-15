import React, { createContext, useState, useEffect } from "react";
import axiosClient from "../api/Client";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("token") || null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(false);
  }, [token]);

  const login = async (username, password) => {
  const response = await axiosClient.post("/users/login", { username, password });
  const { access_token } = response.data;
  localStorage.setItem("token", access_token);
  setToken(access_token);
  return response.data;
};

  const register = async (userData) => {
    const response = await axiosClient.post("/users/register", userData);
    return response.data;
  };

  const logout = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  return (
    <AuthContext.Provider value={{ token, login, register, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};
