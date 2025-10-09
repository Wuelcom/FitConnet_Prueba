import React, { createContext, useState, useEffect } from "react";
import API from "../api";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) { setLoading(false); return; }
    API.get("/api/usuarios/me")
      .then(res => setUser(res.data))
      .catch(() => {
        localStorage.removeItem("token");
        setUser(null);
      })
      .finally(()=> setLoading(false));
  }, []);

  // login usando form-urlencoded a /api/auth/login
  const login = async (email, password) => {
    const params = new URLSearchParams();
    params.append("username", email);
    params.append("password", password);
    const res = await API.post("/api/auth/login", params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
    const token = res.data.access_token;
    localStorage.setItem("token", token);
    // recuperar perfil
    const me = await API.get("/api/usuarios/me");
    setUser(me.data);
    return me.data;
  };

  // register via /api/usuarios
  const register = async (payload) => {
    const res = await API.post("/api/usuarios/", payload);
    // no devuelve token por defecto; auto-login:
    await login(payload.correo_electronico, payload.contrasena);
    return res.data;
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};
