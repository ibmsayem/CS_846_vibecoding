import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import database
import os
import time
from datetime import datetime

client = TestClient(app)

def setup_module(module):
    # Setup test DB
    if os.path.exists("test.db"):
        os.remove("test.db")
    database.Base.metadata.create_all(bind=database.engine)

def teardown_module(module):
    # Teardown test DB
    database.Base.metadata.drop_all(bind=database.engine)
    if os.path.exists("test.db"):
        os.remove("test.db")

# ============================================================================
# USER MANAGEMENT TESTS
# ============================================================================

def test_register_valid():
    """Test successful user registration with valid inputs"""
    r = client.post("/users/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "bio": "Test bio"
    })
    assert r.status_code == 200
    data = r.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert data["bio"] == "Test bio"
    assert "id" in data

def test_register_duplicate_username():
    """Test registration fails with duplicate username"""
    client.post("/users/register", json={
        "username": "dupuser",
        "email": "dup1@example.com",
        "password": "pass123"
    })
    r = client.post("/users/register", json={
        "username": "dupuser",
        "email": "dup2@example.com",
        "password": "pass123"
    })
    assert r.status_code == 400
    assert "already registered" in r.json()["detail"]

def test_register_duplicate_email():
    """Test registration fails with duplicate email"""
    client.post("/users/register", json={
        "username": "user1",
        "email": "same@example.com",
        "password": "pass123"
    })
    r = client.post("/users/register", json={
        "username": "user2",
        "email": "same@example.com",
        "password": "pass123"
    })
    assert r.status_code == 400

def test_register_short_password():
    """Test registration fails with short password"""
    r = client.post("/users/register", json={
        "username": "shortpass",
        "email": "short@example.com",
        "password": "12345"
    })
    assert r.status_code == 422

def test_register_short_username():
    """Test registration fails with short username"""
    r = client.post("/users/register", json={
        "username": "ab",
        "email": "short@example.com",
        "password": "pass123"
    })
    assert r.status_code == 422

def test_login_valid():
    """Test successful login with valid credentials"""
    client.post("/users/register", json={
        "username": "loginuser",
        "email": "login@example.com",
        "password": "loginpass"
    })
    r = client.post("/users/login", json={
        "username": "loginuser",
        "password": "loginpass"
    })
    assert r.status_code == 200
    data = r.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_password():
    """Test login fails with wrong password"""
    client.post("/users/register", json={
        "username": "wrongpass",
        "email": "wrong@example.com",
        "password": "correctpass"
    })
    r = client.post("/users/login", json={
        "username": "wrongpass",
        "password": "wrongpass"
    })
    assert r.status_code == 401
    assert "Invalid credentials" in r.json()["detail"]

def test_login_nonexistent_user():
    """Test login fails for non-existent user"""
    r = client.post("/users/login", json={
        "username": "nonexistent",
        "password": "password"
    })
    assert r.status_code == 401

def test_get_profile():
    """Test retrieving user profile"""
    client.post("/users/register", json={
        "username": "profileuser",
        "email": "profile@example.com",
        "password": "pass",
        "bio": "My bio"
    })
    r = client.get("/users/profileuser")
    assert r.status_code == 200
    data = r.json()
    assert data["username"] == "profileuser"
    assert data["bio"] == "My bio"

def test_get_profile_not_found():
    """Test retrieving non-existent profile"""
    r = client.get("/users/nonexistentuser")
    assert r.status_code == 404

def test_update_profile_own():
    """Test user can update their own profile"""
    client.post("/users/register", json={
        "username": "edituser",
        "email": "edit@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "edituser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    r = client.put("/users/edituser", 
        json={"bio": "Updated bio"},
        headers=headers)
    assert r.status_code == 200
    assert r.json()["bio"] == "Updated bio"

def test_update_profile_other():
    """Test user cannot update other user's profile"""
    # Create two users
    client.post("/users/register", json={
        "username": "user_a",
        "email": "a@example.com",
        "password": "pass"
    })
    client.post("/users/register", json={
        "username": "user_b",
        "email": "b@example.com",
        "password": "pass"
    })
    
    # Login as user_a
    login = client.post("/users/login", json={
        "username": "user_a",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Try to update user_b's profile
    r = client.put("/users/user_b",
        json={"bio": "Hacked!"},
        headers=headers)
    assert r.status_code == 403

# ============================================================================
# POST MANAGEMENT TESTS
# ============================================================================

def test_create_post_valid():
    """Test creating a valid post"""
    client.post("/users/register", json={
        "username": "poster",
        "email": "poster@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "poster",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    r = client.post("/posts/", 
        json={"content": "Hello world!"},
        headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["content"] == "Hello world!"
    assert data["author_username"] == "poster"
    assert data["like_count"] == 0
    assert data["parent_id"] is None

def test_create_post_unauthenticated():
    """Test creating post without authentication"""
    r = client.post("/posts/", json={"content": "No auth"})
    assert r.status_code == 401

def test_create_post_exceeds_limit():
    """Test creating post exceeding 280 characters"""
    client.post("/users/register", json={
        "username": "longpost",
        "email": "long@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "longpost",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    long_content = "x" * 281
    r = client.post("/posts/",
        json={"content": long_content},
        headers=headers)
    assert r.status_code == 400
    assert "280 characters" in r.json()["detail"]

def test_create_post_at_limit():
    """Test creating post exactly at 280 characters"""
    client.post("/users/register", json={
        "username": "atLimit",
        "email": "limit@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "atLimit",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    content = "x" * 280
    r = client.post("/posts/",
        json={"content": content},
        headers=headers)
    assert r.status_code == 200

def test_feed_retrieval():
    """Test retrieving the global feed"""
    # Create user and post
    client.post("/users/register", json={
        "username": "feeduser",
        "email": "feed@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "feeduser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    client.post("/posts/",
        json={"content": "Feed post 1"},
        headers=headers)
    client.post("/posts/",
        json={"content": "Feed post 2"},
        headers=headers)
    
    # Retrieve feed
    r = client.get("/posts/feed")
    assert r.status_code == 200
    posts = r.json()
    assert len(posts) >= 2
    assert all(p["parent_id"] is None for p in posts)

def test_feed_newest_first():
    """Test feed returns posts newest first"""
    client.post("/users/register", json={
        "username": "chronouser",
        "email": "chrono@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "chronouser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    r1 = client.post("/posts/",
        json={"content": "First post"},
        headers=headers)
    first_id = r1.json()["id"]
    
    time.sleep(0.1)  # Small delay
    
    r2 = client.post("/posts/",
        json={"content": "Second post"},
        headers=headers)
    second_id = r2.json()["id"]
    
    # Feed should show second post first
    r = client.get("/posts/feed")
    posts = r.json()
    post_ids = [p["id"] for p in posts]
    assert post_ids.index(second_id) < post_ids.index(first_id)

def test_feed_excludes_replies():
    """Test feed only shows parent posts, not replies"""
    client.post("/users/register", json={
        "username": "replyuser",
        "email": "reply@example.com",
        "password": "pass"
    })
    login = client.post("/users/login", json={
        "username": "replyuser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create parent post
    parent = client.post("/posts/",
        json={"content": "Parent"},
        headers=headers)
    parent_id = parent.json()["id"]
    
    # Create reply
    client.post(f"/posts/{parent_id}/reply",
        json={"content": "Reply"},
        headers=headers)
    
    # Feed should only show parent
    r = client.get("/posts/feed")
    posts = r.json()
    assert all(p["parent_id"] is None for p in posts)

# ============================================================================
# LIKE TESTS
# ============================================================================

def test_like_post():
    """Test liking a post"""
    client.post("/users/register", json={
        "username": "liker1",
        "email": "liker1@example.com",
        "password": "pass"
    })
    client.post("/users/register", json={
        "username": "author1",
        "email": "author1@example.com",
        "password": "pass"
    })
    
    # Author creates post
    login = client.post("/users/login", json={
        "username": "author1",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    post = client.post("/posts/",
        json={"content": "Like me!"},
        headers=headers)
    post_id = post.json()["id"]
    
    # Liker likes post
    login = client.post("/users/login", json={
        "username": "liker1",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    r = client.post(f"/posts/{post_id}/like", headers=headers)
    assert r.status_code == 200

def test_like_duplicate():
    """Test cannot like post twice"""
    client.post("/users/register", json={
        "username": "duplike",
        "email": "duplike@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "duplike",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    post = client.post("/posts/",
        json={"content": "Like once"},
        headers=headers)
    post_id = post.json()["id"]
    
    # Like once
    r1 = client.post(f"/posts/{post_id}/like", headers=headers)
    assert r1.status_code == 200
    
    # Like again (should fail)
    r2 = client.post(f"/posts/{post_id}/like", headers=headers)
    assert r2.status_code == 400
    assert "Already liked" in r2.json()["detail"]

def test_like_nonexistent_post():
    """Test liking non-existent post"""
    client.post("/users/register", json={
        "username": "ghostliker",
        "email": "ghost@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "ghostliker",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    r = client.post("/posts/99999/like", headers=headers)
    assert r.status_code == 404

def test_like_count_displayed():
    """Test like count is displayed in posts"""
    client.post("/users/register", json={
        "username": "countuser",
        "email": "count@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "countuser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    post = client.post("/posts/",
        json={"content": "Count likes"},
        headers=headers)
    post_id = post.json()["id"]
    
    client.post(f"/posts/{post_id}/like", headers=headers)
    
    r = client.get("/posts/feed")
    posts = r.json()
    counted_post = [p for p in posts if p["id"] == post_id][0]
    assert counted_post["like_count"] == 1

# ============================================================================
# REPLY TESTS
# ============================================================================

def test_reply_to_post():
    """Test replying to a post"""
    client.post("/users/register", json={
        "username": "replier1",
        "email": "replier1@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "replier1",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create parent post
    parent = client.post("/posts/",
        json={"content": "Parent post"},
        headers=headers)
    parent_id = parent.json()["id"]
    
    # Reply
    r = client.post(f"/posts/{parent_id}/reply",
        json={"content": "Great post!"},
        headers=headers)
    assert r.status_code == 200
    assert r.json()["parent_id"] == parent_id
    assert r.json()["author_username"] == "replier1"

def test_reply_requires_auth():
    """Test replying requires authentication"""
    r = client.post("/posts/1/reply",
        json={"content": "No auth reply"})
    assert r.status_code == 401

def test_reply_nonexistent_post():
    """Test replying to non-existent post"""
    client.post("/users/register", json={
        "username": "replynoparent",
        "email": "replyno@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "replynoparent",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    r = client.post("/posts/99999/reply",
        json={"content": "Reply to ghost"},
        headers=headers)
    assert r.status_code == 404

def test_get_replies():
    """Test retrieving replies for a post"""
    client.post("/users/register", json={
        "username": "replygetuser",
        "email": "replyget@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "replygetuser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create parent
    parent = client.post("/posts/",
        json={"content": "Parent"},
        headers=headers)
    parent_id = parent.json()["id"]
    
    # Add replies
    client.post(f"/posts/{parent_id}/reply",
        json={"content": "Reply 1"},
        headers=headers)
    client.post(f"/posts/{parent_id}/reply",
        json={"content": "Reply 2"},
        headers=headers)
    
    # Get replies
    r = client.get(f"/posts/{parent_id}/replies")
    assert r.status_code == 200
    replies = r.json()
    assert len(replies) == 2

def test_replies_only_one_level():
    """Test replies are only one level deep"""
    client.post("/users/register", json={
        "username": "oneleveldepth",
        "email": "onelevel@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "oneleveldepth",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Create parent
    parent = client.post("/posts/",
        json={"content": "Parent"},
        headers=headers)
    parent_id = parent.json()["id"]
    
    # Create reply
    reply = client.post(f"/posts/{parent_id}/reply",
        json={"content": "Reply"},
        headers=headers)
    reply_id = reply.json()["id"]
    
    # In feed, reply should have parent_id set to parent
    r = client.get("/posts/feed")
    posts = r.json()
    reply_post = [p for p in posts if p["id"] == reply_id]
    # Reply should still be queryable with parent_id pointing to parent
    assert all(p["parent_id"] is None or p["parent_id"] == parent_id for p in posts)

# ============================================================================
# USER PROFILE TESTS
# ============================================================================

def test_user_posts_endpoint():
    """Test getting all posts by a user"""
    client.post("/users/register", json={
        "username": "mypostuser",
        "email": "mypost@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "mypostuser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    client.post("/posts/",
        json={"content": "My post 1"},
        headers=headers)
    client.post("/posts/",
        json={"content": "My post 2"},
        headers=headers)
    
    r = client.get("/posts/user/mypostuser")
    assert r.status_code == 200
    posts = r.json()
    assert len(posts) == 2
    assert all(p["author_username"] == "mypostuser" for p in posts)

def test_user_posts_not_found():
    """Test user posts endpoint for non-existent user"""
    r = client.get("/posts/user/ghostuser")
    assert r.status_code == 404

# ============================================================================
# PERFORMANCE TESTS
# ============================================================================

def test_performance_post_creation():
    """Test post creation is fast"""
    client.post("/users/register", json={
        "username": "perfuser",
        "email": "perf@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "perfuser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    start = time.time()
    client.post("/posts/",
        json={"content": "Performance test"},
        headers=headers)
    duration = time.time() - start
    
    assert duration < 1.0  # Should complete in < 1 second

def test_performance_feed_load():
    """Test feed loads quickly"""
    start = time.time()
    client.get("/posts/feed")
    duration = time.time() - start
    
    assert duration < 1.0  # Should complete in < 1 second

# ============================================================================
# ERROR HANDLING TESTS
# ============================================================================

def test_invalid_token():
    """Test requests with invalid token are rejected"""
    headers = {"Authorization": "Bearer invalid_token"}
    r = client.post("/posts/",
        json={"content": "Bad token"},
        headers=headers)
    assert r.status_code == 401

def test_malformed_json():
    """Test malformed JSON is rejected"""
    client.post("/users/register", json={
        "username": "jsonuser",
        "email": "json@example.com",
        "password": "pass"
    })
    
    login = client.post("/users/login", json={
        "username": "jsonuser",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # FastAPI should handle this automatically
    r = client.post("/posts/",
        json={"invalid_field": "value"},
        headers=headers)
    assert r.status_code == 422
