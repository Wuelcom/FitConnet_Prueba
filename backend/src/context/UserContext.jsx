import { createContext, useContext, useState, useEffect } from "react";

const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const stored = localStorage.getItem("user");
    if (stored) setUser(JSON.parse(stored));
  }, []);

  const login = (email, password) => {
    const storedUsers = JSON.parse(localStorage.getItem("users")) || [];
    const found = storedUsers.find(
      (u) => u.email === email && u.password === password
    );
    if (found) {
      setUser(found);
      localStorage.setItem("user", JSON.stringify(found));
      return true;
    }
    return false;
  };

  const register = (name, email, password) => {
    const users = JSON.parse(localStorage.getItem("users")) || [];
    const exists = users.find((u) => u.email === email);
    if (exists) return false;
    const newUser = { name, email, password };
    users.push(newUser);
    localStorage.setItem("users", JSON.stringify(users));
    return true;
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("user");
  };

  return (
    <UserContext.Provider value={{ user, login, register, logout }}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = () => useContext(UserContext);
