import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [bio, setBio] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async e => {
    e.preventDefault();
    setError('');
    setLoading(true);

    if (username.length < 3) {
      setError('Username must be at least 3 characters');
      setLoading(false);
      return;
    }

    if (password.length < 6) {
      setError('Password must be at least 6 characters');
      setLoading(false);
      return;
    }

    try {
      await axios.post('/api/users/register', { username, email, password, bio });
      navigate('/login');
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2 className="form-title">Create Account</h2>
      <p className="form-subtitle">Join VibeCode and start sharing your thoughts</p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="form-label">Username</label>
          <input 
            type="text"
            className="form-input"
            placeholder="Choose a username"
            value={username} 
            onChange={e => setUsername(e.target.value)} 
            required 
          />
          <small style={{ fontSize: 12, color: '#536471' }}>3-50 characters</small>
        </div>

        <div className="form-group">
          <label className="form-label">Email</label>
          <input 
            type="email"
            className="form-input"
            placeholder="Enter your email"
            value={email} 
            onChange={e => setEmail(e.target.value)} 
            required 
          />
        </div>

        <div className="form-group">
          <label className="form-label">Password</label>
          <input 
            type="password"
            className="form-input"
            placeholder="Create a password"
            value={password} 
            onChange={e => setPassword(e.target.value)} 
            required 
          />
          <small style={{ fontSize: 12, color: '#536471' }}>At least 6 characters</small>
        </div>

        <div className="form-group">
          <label className="form-label">Bio (Optional)</label>
          <textarea 
            className="form-textarea"
            placeholder="Tell us about yourself"
            value={bio} 
            onChange={e => setBio(e.target.value)} 
            maxLength={160}
            style={{ minHeight: 80 }}
          />
          <small style={{ fontSize: 12, color: '#536471' }}>{bio.length}/160</small>
        </div>

        {error && <div className="error-message">{error}</div>}
        
        <button type="submit" className="form-button" disabled={loading}>
          {loading ? 'Creating account...' : 'Create Account'}
        </button>
      </form>

      <div className="form-link">
        Already have an account? <Link to="/login">Sign in here</Link>
      </div>
    </div>
  );
}

export default Register;
