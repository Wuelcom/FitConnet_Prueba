import React, { useState } from "react";
import API from "../api";
import { useNavigate } from "react-router-dom";

export default function EjercicioForm(){
  const [form, setForm] = useState({ nombre: "", descripcion: "", grupo_muscular: "" });
  const nav = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await API.post("/api/ejercicios", form);
      nav("/ejercicios");
    } catch (err) {
      console.error(err);
      alert("Error creando ejercicio");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="nombre" value={form.nombre} onChange={e=>setForm({...form, nombre:e.target.value})} placeholder="Nombre" required/>
      <textarea name="descripcion" value={form.descripcion} onChange={e=>setForm({...form, descripcion:e.target.value})} placeholder="Descripcion"/>
      <input name="grupo_muscular" value={form.grupo_muscular} onChange={e=>setForm({...form, grupo_muscular:e.target.value})} placeholder="Grupo muscular"/>
      <button type="submit">Guardar</button>
    </form>
  );
}
