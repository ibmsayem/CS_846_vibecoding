
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import Feed from './pages/Feed';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import './App.css';

function NavBar({ user, setUser }) {
  const navigate = useNavigate();
  const handleLogout = () => {
    localStorage.removeItem('token');
    setUser(null);
    navigate('/');
  };
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-logo">
          <Link to="/">
            <span className="logo-icon">💬</span>
            <span className="logo-text">VibeCode</span>
          </Link>
        </div>
        <div className="navbar-links">
          <Link to="/" className="nav-link">Feed</Link>
          {user ? (
            <>
              <Link to={`/profile/${user}`} className="nav-link">👤 {user}</Link>
              <button onClick={handleLogout} className="nav-button logout-btn">Logout</button>
            </>
          ) : (
            <>
              <Link to="/login" className="nav-link">Login</Link>
              <Link to="/register" className="nav-link">Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

function App() {
  const [user, setUser] = useState(null);
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        setUser(payload.sub);
      } catch {
        setUser(null);
      }
    } else {
      setUser(null);
    }
  }, []);
  return (
    <Router>
      <div className="app-container">
        <NavBar user={user} setUser={setUser} />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Feed />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/profile/:username" element={<Profile />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
