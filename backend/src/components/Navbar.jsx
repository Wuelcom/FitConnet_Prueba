import { Link } from "react-router-dom";
import "./Navbar.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">🏋️‍♂️ FitConnet</div>
      <ul className="nav-links">
        <li><Link to="/">Inicio</Link></li>
        <li><Link to="/planes">Planes</Link></li>
        <li><Link to="/contacto">Contacto</Link></li>
        <li><Link to="/login">Iniciar sesión</Link></li>
        <li><Link to="/register">Registrarse</Link></li>
      </ul>
    </nav>
  );
}
