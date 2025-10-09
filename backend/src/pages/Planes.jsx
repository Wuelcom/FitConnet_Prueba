const planes = [
  { nombre: "Básico", precio: "$20.000", beneficios: ["Rutinas básicas", "Acceso limitado"] },
  { nombre: "Pro", precio: "$50.000", beneficios: ["Rutinas completas", "Asesoría personalizada"] },
  { nombre: "Premium", precio: "$80.000", beneficios: ["Todo incluido", "Entrenador 24/7"] },
];

export default function Planes() {
  return (
    <section>
      <h2>Planes disponibles</h2>
      <div className="planes-grid">
        {planes.map((p) => (
          <div className="plan-card" key={p.nombre}>
            <h3>{p.nombre}</h3>
            <p>{p.precio}</p>
            <ul>
              {p.beneficios.map((b, i) => <li key={i}>{b}</li>)}
            </ul>
          </div>
        ))}
      </div>
    </section>
  );
}
