import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function Profile() {
  const { username } = useParams();
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [editBio, setEditBio] = useState('');
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState('');
  const token = localStorage.getItem('token');
  const currentUser = token ? JSON.parse(atob(token.split('.')[1])).sub : null;
  const isOwnProfile = currentUser === username;

  useEffect(() => {
    setLoading(true);
    Promise.all([
      axios.get(`/api/users/${username}`).then(res => {
        setUser(res.data);
        setEditBio(res.data.bio || '');
      }),
      axios.get(`/api/posts/user/${username}`).then(res => setPosts(res.data))
    ]).finally(() => setLoading(false));
  }, [username]);

  const handleSaveBio = async () => {
    try {
      setSaving(true);
      const response = await axios.put(
        `/api/users/${username}`,
        { bio: editBio },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setUser(response.data);
      setIsEditing(false);
      setMessage('✅ Bio updated successfully!');
      setTimeout(() => setMessage(''), 3000);
    } catch (error) {
      setMessage('❌ Failed to update bio: ' + (error.response?.data?.detail || 'Error'));
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', padding: 48, fontSize: 16, color: '#536471' }}>
        Loading profile...
      </div>
    );
  }

  if (!user) {
    return (
      <div style={{ textAlign: 'center', padding: 48, fontSize: 16, color: '#e7245e' }}>
        User not found
      </div>
    );
  }

  return (
    <div className="profile-container">
      <div className="profile-header">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2 className="profile-username">@{user.username}</h2>
          {isOwnProfile && !isEditing && (
            <button onClick={() => setIsEditing(true)} className="nav-button" style={{ fontSize: 14 }}>
              ✏️ Edit Profile
            </button>
          )}
        </div>

        {isEditing ? (
          <div style={{ marginTop: 16 }}>
            <textarea
              value={editBio}
              onChange={(e) => setEditBio(e.target.value)}
              placeholder="Add your bio..."
              maxLength="160"
              className="form-input"
              style={{ minHeight: 80, padding: 12 }}
            />
            <div style={{ fontSize: 12, color: '#536471', marginTop: 8, marginBottom: 12 }}>
              {editBio.length}/160 characters
            </div>
            <div style={{ display: 'flex', gap: 12 }}>
              <button
                onClick={handleSaveBio}
                className="nav-button"
                disabled={saving}
                style={{ backgroundColor: '#1da1f2' }}
              >
                {saving ? 'Saving...' : '💾 Save'}
              </button>
              <button
                onClick={() => {
                  setIsEditing(false);
                  setEditBio(user.bio || '');
                  setMessage('');
                }}
                className="nav-button"
                style={{ backgroundColor: '#536471' }}
              >
                Cancel
              </button>
            </div>
          </div>
        ) : (
          <p className="profile-bio">{user.bio || '📝 No bio added yet'}</p>
        )}

        {message && (
          <div style={{
            marginTop: 12,
            padding: 12,
            backgroundColor: message.includes('✅') ? '#f0fdf4' : '#fef2f2',
            borderRadius: 8,
            fontSize: 14,
            color: message.includes('✅') ? '#166534' : '#991b1b'
          }}>
            {message}
          </div>
        )}

        <div className="profile-stats">
          <div className="profile-stat">
            <div className="profile-stat-value">{posts.length}</div>
            <div className="profile-stat-label">Posts</div>
          </div>
        </div>
      </div>

      <div>
        <h3 style={{ marginBottom: 16, fontSize: 20, fontWeight: 700 }}>Posts</h3>
        {posts.length === 0 ? (
          <div style={{
            background: 'white',
            padding: 32,
            borderRadius: 12,
            textAlign: 'center',
            color: '#536471'
          }}>
            No posts yet
          </div>
        ) : (
          <div className="profile-posts">
            {posts.map(post => (
              <div key={post.id} className="post-card">
                <p className="post-content">{post.content}</p>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 12 }}>
                  <span className="post-timestamp">
                    {new Date(post.created_at).toLocaleDateString('en-US', {
                      month: 'short',
                      day: 'numeric',
                      hour: '2-digit',
                      minute: '2-digit'
                    })}
                  </span>
                  <span style={{ fontSize: 12, color: '#536471' }}>
                    ❤️ {post.like_count} {post.like_count === 1 ? 'like' : 'likes'}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default Profile;
