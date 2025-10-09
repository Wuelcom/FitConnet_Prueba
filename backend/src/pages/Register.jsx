import React, { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext";

export default function Register(){
  const { register } = useContext(AuthContext);
  const nav = useNavigate();
  const [form, setForm] = useState({
    nombre: "", correo_electronico: "", contrasena: "", telefono: ""
  });
  const [err, setErr] = useState(null);

  const handleChange = e => setForm({...form, [e.target.name]: e.target.value});

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await register(form);
      nav("/user");
    } catch (error) {
      setErr(error?.response?.data?.detail || "Error registrando");
    }
  };

  return (
    <div>
      <h2>Registro</h2>
      <form onSubmit={handleSubmit}>
        <input name="nombre" placeholder="Nombre" value={form.nombre} onChange={handleChange} required/>
        <input name="correo_electronico" placeholder="Email" value={form.correo_electronico} onChange={handleChange} required/>
        <input name="contrasena" placeholder="Contraseña" value={form.contrasena} onChange={handleChange} type="password" required/>
        <input name="telefono" placeholder="Teléfono" value={form.telefono} onChange={handleChange}/>
        <button type="submit">Crear cuenta</button>
      </form>
      {err && <p style={{color:'red'}}>{err}</p>}
    </div>
  );
}
