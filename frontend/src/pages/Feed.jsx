
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Feed() {
  const [posts, setPosts] = useState([]);
  const [replies, setReplies] = useState({}); // Store replies by post ID
  const [content, setContent] = useState("");
  const [replyContent, setReplyContent] = useState("");
  const [replyTo, setReplyTo] = useState(null);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [expandedPosts, setExpandedPosts] = useState({}); // Track which posts have expanded replies
  const token = localStorage.getItem('token');
  let username = null;
  if (token) {
    try {
      username = JSON.parse(atob(token.split('.')[1])).sub;
    } catch {}
  }

  const fetchPosts = () => {
    axios.get('/api/posts/feed').then(res => setPosts(res.data));
  };

  const fetchReplies = async (postId) => {
    try {
      const res = await axios.get(`/api/posts/${postId}/replies`);
      setReplies(prev => ({ ...prev, [postId]: res.data }));
      setExpandedPosts(prev => ({ ...prev, [postId]: true }));
    } catch (err) {
      console.error('Failed to fetch replies:', err);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  const handlePost = async e => {
    e.preventDefault();
    setError(""); 
    setSuccess("");
    if (!content.trim()) {
      setError("Post cannot be empty");
      return;
    }
    try {
      await axios.post('/api/posts/', { content }, { headers: { Authorization: `Bearer ${token}` } });
      setContent("");
      setSuccess("Posted successfully!");
      setTimeout(() => setSuccess(""), 3000);
      fetchPosts();
    } catch (err) {
      setError("Failed to post. Are you logged in?");
    }
  };

  const handleLike = async postId => {
    try {
      await axios.post(`/api/posts/${postId}/like`, {}, { headers: { Authorization: `Bearer ${token}` } });
      fetchPosts();
    } catch {}
  };

  const handleReply = async (e, postId) => {
    e.preventDefault();
    if (!replyContent.trim()) {
      return;
    }
    try {
      await axios.post(`/api/posts/${postId}/reply`, { content: replyContent }, { headers: { Authorization: `Bearer ${token}` } });
      setReplyContent("");
      setReplyTo(null);
      fetchPosts();
      // Refresh replies if post is expanded
      if (expandedPosts[postId]) {
        fetchReplies(postId);
      }
    } catch {}
  };

  return (
    <div className="feed-container">
      <h1 style={{ marginBottom: 24, fontSize: 32, fontWeight: 700 }}>Global Feed</h1>
      {username && (
        <form onSubmit={handlePost} className="post-form">
          <textarea 
            value={content} 
            onChange={e => setContent(e.target.value)} 
            maxLength={280} 
            placeholder="What's happening?!"
            required
          />
          <div className="post-form-actions">
            <span style={{ fontSize: 12, color: '#536471' }}>
              {content.length}/280
            </span>
            <button type="submit" className="post-form-button">Post</button>
          </div>
          {error && <div className="error-message">{error}</div>}
          {success && <div className="success-message">{success}</div>}
        </form>
      )}
      {!username && (
        <div style={{ 
          textAlign: 'center', 
          padding: 32, 
          background: '#f7f9fa', 
          borderRadius: 12,
          marginBottom: 24
        }}>
          <p style={{ fontSize: 16, color: '#536471', marginBottom: 16 }}>
            Please login or register to post
          </p>
          <a href="/login" style={{ 
            display: 'inline-block',
            padding: '10px 24px',
            backgroundColor: '#1da1f2',
            color: 'white',
            textDecoration: 'none',
            borderRadius: 20,
            fontWeight: 600,
            marginRight: 12
          }}>Login</a>
          <a href="/register" style={{ 
            display: 'inline-block',
            padding: '10px 24px',
            backgroundColor: '#f91880',
            color: 'white',
            textDecoration: 'none',
            borderRadius: 20,
            fontWeight: 600
          }}>Register</a>
        </div>
      )}
      <div style={{ marginTop: 16 }}>
        {posts.length === 0 ? (
          <div style={{ 
            textAlign: 'center', 
            padding: 48,
            background: 'white',
            borderRadius: 12,
            color: '#536471'
          }}>
            <p style={{ fontSize: 16 }}>No posts yet. Be the first to post! 🚀</p>
          </div>
        ) : (
          posts.map(post => (
            <div key={post.id}>
              <div className="post-card">
                <div className="post-header">
                  <Link to={`/profile/${post.author_username}`} className="post-author">
                    @{post.author_username || `User ${post.author_id}`}
                  </Link>
                  <span className="post-timestamp">
                    {new Date(post.created_at).toLocaleDateString('en-US', { 
                      month: 'short', 
                      day: 'numeric',
                      hour: '2-digit',
                      minute: '2-digit'
                    })}
                  </span>
                </div>
                <p className="post-content">{post.content}</p>
                {username && (
                  <div className="post-actions">
                    <button 
                      onClick={() => handleLike(post.id)} 
                      className="post-button"
                    >
                      ❤️ Like {post.like_count > 0 && `(${post.like_count})`}
                    </button>
                    <button 
                      onClick={() => setReplyTo(post.id)}
                      className="post-button"
                    >
                      💬 Reply
                    </button>
                    <button
                      onClick={() => {
                        if (expandedPosts[post.id]) {
                          setExpandedPosts(prev => ({ ...prev, [post.id]: false }));
                        } else {
                          fetchReplies(post.id);
                        }
                      }}
                      className="post-button"
                      style={{ fontSize: 12 }}
                    >
                      {expandedPosts[post.id] ? '🔽 Hide Replies' : '💭 View Replies'}
                    </button>
                  </div>
                )}
                {!username && (
                  <div style={{ fontSize: 12, color: '#536471', padding: '12px 0', fontStyle: 'italic' }}>
                    💭 {replies[post.id]?.length || 0} {(replies[post.id]?.length || 0) === 1 ? 'reply' : 'replies'}
                  </div>
                )}
                {username && replyTo === post.id && (
                  <form onSubmit={e => handleReply(e, post.id)} className="reply-form">
                    <input 
                      type="text"
                      value={replyContent} 
                      onChange={e => setReplyContent(e.target.value)} 
                      maxLength={280} 
                      placeholder="Reply..."
                      className="reply-input"
                      required 
                    />
                    <div className="reply-actions">
                      <button type="submit" className="reply-button">Send</button>
                      <button 
                        type="button" 
                        onClick={() => setReplyTo(null)}
                        className="reply-button reply-cancel"
                      >
                        Cancel
                      </button>
                    </div>
                  </form>
                )}
              </div>

              {/* Display nested replies */}
              {expandedPosts[post.id] && replies[post.id] && replies[post.id].length > 0 && (
                <div style={{ marginLeft: 16, borderLeft: '2px solid #eff3f4', paddingLeft: 16, marginBottom: 16 }}>
                  <div style={{ fontSize: 12, color: '#536471', marginBottom: 12, fontStyle: 'italic' }}>
                    💭 {replies[post.id].length} {replies[post.id].length === 1 ? 'reply' : 'replies'}
                  </div>
                  {replies[post.id].map(reply => (
                    <div key={reply.id} className="post-card" style={{ marginBottom: 12, backgroundColor: '#f7f9fa' }}>
                      <div className="post-header">
                        <Link to={`/profile/${reply.author_username}`} className="post-author">
                          @{reply.author_username || `User ${reply.author_id}`}
                        </Link>
                        <span className="post-timestamp">
                          {new Date(reply.created_at).toLocaleDateString('en-US', { 
                            month: 'short', 
                            day: 'numeric',
                            hour: '2-digit',
                            minute: '2-digit'
                          })}
                        </span>
                      </div>
                      <p className="post-content" style={{ fontSize: 14 }}>{reply.content}</p>
                      {username && (
                        <div className="post-actions">
                          <button 
                            onClick={() => handleLike(reply.id)} 
                            className="post-button"
                            style={{ fontSize: 12 }}
                          >
                            ❤️ Like {reply.like_count > 0 && `(${reply.like_count})`}
                          </button>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
              {expandedPosts[post.id] && (!replies[post.id] || replies[post.id].length === 0) && (
                <div style={{ marginLeft: 16, paddingLeft: 16, paddingBottom: 16, color: '#536471', fontSize: 14, fontStyle: 'italic' }}>
                  No replies yet
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Feed;
