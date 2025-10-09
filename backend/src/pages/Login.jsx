import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext";

export default function Login(){
  const [email, setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [err, setErr] = useState(null);
  const { login } = useContext(AuthContext);
  const nav = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const user = await login(email, password);
      // no hay un role en el schema por defecto, si tu DB lo tiene usa user.role
      nav("/user");
    } catch (error) {
      setErr(error?.response?.data?.detail || "Credenciales inválidas");
    }
  };

  return (
    <div>
      <h2>Iniciar sesión</h2>
      <form onSubmit={handleSubmit}>
        <input value={email} onChange={e=>setEmail(e.target.value)} type="email" placeholder="Correo"/> 
        <input value={password} onChange={e=>setPassword(e.target.value)} type="password" placeholder="Contraseña"/>
        <button type="submit">Entrar</button>
      </form>
      {err && <p style={{color:'red'}}>{err}</p>}
    </div>
  );
}
