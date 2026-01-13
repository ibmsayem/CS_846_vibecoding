# 📡 VibeCode API Documentation

## Base URL
```
http://localhost:8001/api
```

## Authentication
All protected endpoints require a JWT token in the `Authorization` header:
```
Authorization: Bearer <your_jwt_token>
```

---

## 👤 User Endpoints

### 1. Register User
Create a new user account.

**Endpoint:**
```
POST /users/register
```

**Content-Type:** `application/json`

**Request Body:**
```json
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "password123",
  "bio": "I love coding"
}
```

**Parameters:**
| Field | Type | Required | Constraints |
|-------|------|----------|------------|
| username | string | Yes | 3-50 characters, must be unique |
| email | string | Yes | Valid email format, must be unique |
| password | string | Yes | Min 6 characters, max 72 bytes |
| bio | string | No | Max 160 characters |

**Success Response (200):**
```json
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "I love coding"
}
```

**Error Responses:**
```json
// 400 - Username/Email already exists
{
  "detail": "Username or email already registered"
}

// 422 - Invalid input
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "username"],
      "msg": "ensure this value has at least 3 characters"
    }
  ]
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8001/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "email": "alice@example.com",
    "password": "password123",
    "bio": "I love coding"
  }'
```

---

### 2. Login User
Authenticate user and get JWT token.

**Endpoint:**
```
POST /users/login
```

**Content-Type:** `application/json`

**Request Body:**
```json
{
  "username": "alice",
  "password": "password123"
}
```

**Parameters:**
| Field | Type | Required |
|-------|------|----------|
| username | string | Yes |
| password | string | Yes |

**Success Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsImV4cCI6MTc2ODMzNDIxMn0.amYNb5riJljsFSs1L8c8Dbtf8B90yeWGz0I7Y9n2klo",
  "token_type": "bearer"
}
```

**Error Responses:**
```json
// 401 - Invalid credentials
{
  "detail": "Invalid credentials"
}
```

**Token Details:**
- **Type**: JWT (JSON Web Token)
- **Algorithm**: HS256
- **Expiration**: 60 minutes from login time
- **Payload**: 
  ```json
  {
    "sub": "alice",    // username
    "exp": 1768334212   // expiration timestamp
  }
  ```

**cURL Example:**
```bash
curl -X POST http://localhost:8001/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice",
    "password": "password123"
  }'
```

---

### 3. Get User Profile
Retrieve user information by username.

**Endpoint:**
```
GET /users/{username}
```

**Parameters:**
| Parameter | Type | Location | Required |
|-----------|------|----------|----------|
| username | string | URL path | Yes |

**Success Response (200):**
```json
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "I love coding"
}
```

**Error Responses:**
```json
// 404 - User not found
{
  "detail": "User not found"
}
```

**cURL Example:**
```bash
curl -X GET http://localhost:8001/api/users/alice
```

---

## 📝 Post Endpoints

### 1. Create Post
Create a new post (requires authentication).

**Endpoint:**
```
POST /posts/
```

**Content-Type:** `application/json`
**Authentication:** Required ✅

**Request Body:**
```json
{
  "content": "Hello world! This is my first post!",
  "parent_id": null
}
```

**Parameters:**
| Field | Type | Required | Constraints |
|-------|------|----------|------------|
| content | string | Yes | Max 280 characters |
| parent_id | integer | No | ID of post to reply to |

**Success Response (200):**
```json
{
  "id": 1,
  "content": "Hello world! This is my first post!",
  "created_at": "2026-01-13T14:23:45.123456",
  "author_id": 1,
  "author_username": "alice",
  "parent_id": null
}
```

**Error Responses:**
```json
// 400 - Post too long
{
  "detail": "Post exceeds 280 characters"
}

// 401 - Not authenticated
{
  "detail": "Could not validate credentials"
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8001/api/posts/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "content": "Hello world!",
    "parent_id": null
  }'
```

---

### 2. Get Global Feed
Retrieve all posts (chronological order, newest first).

**Endpoint:**
```
GET /posts/feed
```

**Authentication:** Not required ❌

**Query Parameters:** None

**Success Response (200):**
```json
[
  {
    "id": 2,
    "content": "Great day today!",
    "created_at": "2026-01-13T14:30:00.000000",
    "author_id": 2,
    "author_username": "bob",
    "parent_id": null
  },
  {
    "id": 1,
    "content": "Hello world!",
    "created_at": "2026-01-13T14:23:45.123456",
    "author_id": 1,
    "author_username": "alice",
    "parent_id": null
  }
]
```

**Error Responses:**
```json
// 200 - Empty feed
[]
```

**cURL Example:**
```bash
curl -X GET http://localhost:8001/api/posts/feed
```

---

### 3. Get User Posts
Retrieve all posts by a specific user.

**Endpoint:**
```
GET /posts/user/{username}
```

**Authentication:** Not required ❌

**Parameters:**
| Parameter | Type | Location | Required |
|-----------|------|----------|----------|
| username | string | URL path | Yes |

**Success Response (200):**
```json
[
  {
    "id": 1,
    "content": "Hello world!",
    "created_at": "2026-01-13T14:23:45.123456",
    "author_id": 1,
    "author_username": "alice",
    "parent_id": null
  }
]
```

**Error Responses:**
```json
// 404 - User not found
{
  "detail": "User not found"
}
```

**cURL Example:**
```bash
curl -X GET http://localhost:8001/api/posts/user/alice
```

---

### 4. Like Post
Like a post (requires authentication).

**Endpoint:**
```
POST /posts/{post_id}/like
```

**Content-Type:** `application/json`
**Authentication:** Required ✅

**Parameters:**
| Parameter | Type | Location | Required |
|-----------|------|----------|----------|
| post_id | integer | URL path | Yes |

**Request Body:**
```json
{}
```

**Success Response (200):**
```json
{
  "message": "Post liked"
}
```

**Error Responses:**
```json
// 400 - Already liked
{
  "detail": "Already liked"
}

// 404 - Post not found
{
  "detail": "Post not found"
}

// 401 - Not authenticated
{
  "detail": "Could not validate credentials"
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8001/api/posts/1/like \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{}'
```

---

### 5. Reply to Post
Create a reply to a post (requires authentication).

**Endpoint:**
```
POST /posts/{post_id}/reply
```

**Content-Type:** `application/json`
**Authentication:** Required ✅

**Parameters:**
| Parameter | Type | Location | Required |
|-----------|------|----------|----------|
| post_id | integer | URL path | Yes |

**Request Body:**
```json
{
  "content": "Great post!",
  "parent_id": null
}
```

**Parameters:**
| Field | Type | Required | Constraints |
|-------|------|----------|------------|
| content | string | Yes | Max 280 characters |
| parent_id | integer | No | Leave null, will be set to post_id |

**Success Response (200):**
```json
{
  "id": 2,
  "content": "Great post!",
  "created_at": "2026-01-13T14:35:20.000000",
  "author_id": 2,
  "author_username": "bob",
  "parent_id": 1
}
```

**Error Responses:**
```json
// 404 - Post not found
{
  "detail": "Parent post not found"
}

// 400 - Invalid parent_id
{
  "detail": "Invalid parent_id"
}

// 401 - Not authenticated
{
  "detail": "Could not validate credentials"
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8001/api/posts/1/reply \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "content": "Great post!",
    "parent_id": null
  }'
```

---

## 🔄 Request/Response Lifecycle

### Example: Full User Journey

1. **Register**
```bash
POST /api/users/register
→ 200 OK
```

2. **Login**
```bash
POST /api/users/login
→ 200 OK (get JWT token)
```

3. **Create Post**
```bash
POST /api/posts/
Authorization: Bearer <token>
→ 200 OK
```

4. **Get Feed**
```bash
GET /api/posts/feed
→ 200 OK (see all posts)
```

5. **Like Post**
```bash
POST /api/posts/1/like
Authorization: Bearer <token>
→ 200 OK
```

6. **Reply to Post**
```bash
POST /api/posts/1/reply
Authorization: Bearer <token>
→ 200 OK
```

7. **View Profile**
```bash
GET /api/users/alice
→ 200 OK
```

---

## 🛡️ Error Codes

| Code | Meaning | Possible Causes |
|------|---------|-----------------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid input, post too long, already liked |
| 401 | Unauthorized | Missing/invalid token, invalid credentials |
| 404 | Not Found | User/post doesn't exist |
| 422 | Unprocessable Entity | Invalid data type or format |
| 500 | Server Error | Backend error (check logs) |

---

## 📊 Data Models

### User Object
```json
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "I love coding",
  "created_at": "2026-01-13T14:00:00"
}
```

### Post Object
```json
{
  "id": 1,
  "content": "Hello world!",
  "author_id": 1,
  "author_username": "alice",
  "created_at": "2026-01-13T14:23:45.123456",
  "parent_id": null  // null if not a reply
}
```

### Like Object (Internal)
```json
{
  "id": 1,
  "user_id": 1,
  "post_id": 1,
  "created_at": "2026-01-13T14:25:00"
}
```

---

## 🧪 Testing with cURL

### Complete API Test Script
```bash
#!/bin/bash

BASE_URL="http://localhost:8001/api"

# 1. Register
echo "1. Registering user..."
REGISTER=$(curl -s -X POST $BASE_URL/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "bio": "Test user"
  }')
echo $REGISTER

# 2. Login
echo "2. Logging in..."
LOGIN=$(curl -s -X POST $BASE_URL/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "password123"
  }')
TOKEN=$(echo $LOGIN | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)
echo "Token: $TOKEN"

# 3. Create post
echo "3. Creating post..."
curl -s -X POST $BASE_URL/posts/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"content": "Hello world!", "parent_id": null}' | json_pp

# 4. Get feed
echo "4. Getting feed..."
curl -s -X GET $BASE_URL/posts/feed | json_pp

# 5. Get profile
echo "5. Getting profile..."
curl -s -X GET $BASE_URL/users/testuser | json_pp

echo "✅ API test complete!"
```

---

## 📱 Frontend Usage Examples

### Using axios in React
```javascript
// Login
const loginUser = async (username, password) => {
  const response = await axios.post('/api/users/login', {
    username,
    password
  });
  localStorage.setItem('token', response.data.access_token);
};

// Create post
const createPost = async (content) => {
  const token = localStorage.getItem('token');
  return axios.post('/api/posts/', 
    { content, parent_id: null },
    { headers: { Authorization: `Bearer ${token}` } }
  );
};

// Like post
const likePost = async (postId) => {
  const token = localStorage.getItem('token');
  return axios.post(`/api/posts/${postId}/like`,
    {},
    { headers: { Authorization: `Bearer ${token}` } }
  );
};
```

---

## 🔐 Security Notes

1. **Never share your JWT token**
2. **Tokens expire after 60 minutes** - re-login to get new token
3. **Passwords are bcrypt hashed** - never stored in plain text
4. **Passwords limited to 72 bytes** - bcrypt constraint
5. **All user input is validated** - XSS and injection prevention

---

## 📈 Rate Limiting

Currently **not implemented**. In production, consider:
- Limiting login attempts (5 per minute)
- Limiting posts (10 per hour per user)
- Limiting API requests (100 per minute per IP)

---

**API Documentation v1.0**
**Last Updated**: January 13, 2026
