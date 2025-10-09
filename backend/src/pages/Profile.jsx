import React, { useContext, useEffect, useState } from "react";
import { AuthContext } from "../contexts/AuthContext";
import API from "../api";

export default function Profile(){
  const { user, setUser } = useContext(AuthContext);
  const [progreso, setProgreso] = useState([]);

  useEffect(()=> {
    if (!user) return;
    API.get(`/api/progreso?skip=0&limit=100`)
      .then(res => {
        // si tu backend filtra por user, perfecto; si no, filtra aquí por id_usuario
        const list = res.data.filter(p => p.id_usuario === user.id_usuario);
        setProgreso(list);
      }).catch(()=> setProgreso([]));
  }, [user]);

  const handleSave = async (updates) => {
    try {
      const res = await API.put(`/api/usuarios/${user.id_usuario}`, updates);
      setUser(res.data);
      alert("Perfil actualizado");
    } catch (e) { console.error(e); alert("Error al guardar"); }
  };

  if (!user) return <div>Cargando...</div>;

  return (
    <div>
      <h2>Perfil de {user.nombre}</h2>
      <p>Email: {user.correo_electronico}</p>
      <p>ID: {user.id_usuario}</p>

      <h3>Progreso</h3>
      <ul>
        {progreso.map(p => (<li key={p.id_progreso}>{p.fecha}: {p.valor}</li>))}
      </ul>

      {/* Agrega UI para editar si quieres */}
    </div>
  );
}
