import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [mensaje, setMensaje] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setMensaje("");

    try {
      const res = await fetch("http://localhost:5000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await res.json();

      if (res.ok) {
        localStorage.setItem("token", data.token); // Guarda el token
        setMensaje("✅ Inicio de sesión exitoso");
        navigate("/dashboard"); // Redirige al dashboard
      } else {
        setMensaje(`❌ ${data.error || "Error al iniciar sesión"}`);
      }
    } catch (error) {
      setMensaje("⚠️ Error al conectar con el servidor");
    }
  };

  return (
    <div className="form-container">
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Correo electrónico"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Entrar</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
}

export default Login;
