import React, { useEffect, useState } from "react";
import API from "../api";

export default function EjerciciosList(){
  const [ejercicios, setEjercicios] = useState([]);

  useEffect(()=>{
    API.get("/api/ejercicios")
      .then(res => setEjercicios(res.data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Ejercicios</h2>
      <ul>
        {ejercicios.map(e => (
          <li key={e.id_ejercicio}>
            <h4>{e.nombre}</h4>
            <p>{e.descripcion}</p>
            <small>{e.grupo_muscular}</small>
          </li>
        ))}
      </ul>
    </div>
  );
}
