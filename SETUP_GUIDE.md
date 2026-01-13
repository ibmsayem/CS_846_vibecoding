# 📖 CS846 VibeCode - Complete Setup & Usage Guide

## 🎯 Overview

VibeCode is a full-stack microblogging application with:
- **Backend**: FastAPI REST API with JWT authentication
- **Frontend**: Modern React UI with Vite
- **Database**: SQLite with SQLAlchemy ORM
- **Design**: Professional, responsive UI with smooth animations

---

## 💻 System Requirements

- **Python**: 3.10 or higher
- **Node.js**: 16 or higher  
- **npm**: 8 or higher
- **OS**: macOS, Linux, or Windows
- **RAM**: 2GB minimum
- **Disk**: 500MB free space

---

## 🔧 Step-by-Step Installation

### Step 1: Clone/Extract the Project
```bash
cd /path/to/CS_846_vibecoding
```

### Step 2: Backend Setup

#### Option A: macOS/Linux
```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Verify installation
python -c "import fastapi; print('FastAPI installed')"
```

#### Option B: Windows
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install Node dependencies
npm install

# Verify Vite is installed
npm list vite
```

---

## 🚀 Running the Application

### Terminal 1: Start Backend Server
```bash
cd backend

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Run backend on port 8001
PYTHONPATH=. uvicorn app.main:app --reload --port 8001
```

**Expected output:**
```
Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
```

### Terminal 2: Start Frontend Dev Server
```bash
cd frontend

# Run frontend on port 3000
npm run dev
```

**Expected output:**
```
  VITE v4.x.x  ready in xxx ms
  ➜  Local:   http://localhost:3000/
```

### Terminal 3: (Optional) View Logs
```bash
cd backend

# Watch logs in real-time
tail -f logs/app.log.md
```

### Open in Browser
Visit: **http://localhost:3000**

---

## 📝 User Guide

### 1. Registration (Create Account)

1. Click **"Register"** in the navigation
2. Fill in the form:
   - **Username**: 3-50 characters (alphanumeric)
   - **Email**: Valid email address
   - **Password**: At least 6 characters
   - **Bio**: (Optional) Up to 160 characters
3. Click **"Create Account"**
4. Redirected to login page

**Test Account:**
- Username: `alice`
- Email: `alice@example.com`
- Password: `password123`

### 2. Login (Sign In)

1. Click **"Login"** in the navigation
2. Enter username and password
3. Click **"Sign In"**
4. Redirected to feed

### 3. Create Posts

1. Make sure you're logged in
2. Find the text box at the top of the Feed
3. Type your post (max 280 characters)
4. Character counter shows: `X/280`
5. Click **"Post"** button
6. Post appears immediately in feed

### 4. Interact with Posts

**Like a Post:**
1. Find any post in the feed
2. Click **"❤️ Like"** button
3. Button shows you've liked it

**Reply to a Post:**
1. Find any post in the feed
2. Click **"💬 Reply"** button
3. Reply box appears
4. Type your reply (max 280 chars)
5. Click **"Send"** or **"Cancel"**

### 5. View User Profiles

1. Click on any username (e.g., `@alice`) in the feed
2. See user's profile with bio
3. See all posts by that user
4. Click back to feed in navigation

---

## 🔑 Authentication Flow

```
User Registration/Login
         ↓
Backend validates credentials
         ↓
JWT token generated (60 min expiration)
         ↓
Token stored in browser localStorage
         ↓
Token sent with every API request
         ↓
Backend verifies token
         ↓
Allow/Deny request
```

---

## 🐛 Troubleshooting

### Issue: "Address already in use" (Port 8001 or 3000)

**Solution 1: Kill the process**
```bash
# For port 8001 (Backend)
lsof -i :8001 | grep LISTEN | awk '{print $2}' | xargs kill -9

# For port 3000 (Frontend)
lsof -i :3000 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

**Solution 2: Use different ports**
```bash
# Backend on 8002
PYTHONPATH=. uvicorn app.main:app --port 8002

# Frontend on 3001
npm run dev -- --port 3001

# Update vite.config.js:
proxy: {
  '/api': 'http://localhost:8002'  // Changed from 8001
}
```

### Issue: "ModuleNotFoundError: No module named 'app'"

**Solution**: Missing PYTHONPATH
```bash
# ✅ Correct
PYTHONPATH=. uvicorn app.main:app --reload --port 8001

# ❌ Wrong
uvicorn app.main:app --reload --port 8001
```

### Issue: "Cannot find module" (Frontend)

**Solution**: Install dependencies
```bash
cd frontend
npm install
rm -rf node_modules
npm install
```

### Issue: "Database is locked"

**Solution**: Delete and recreate database
```bash
cd backend
rm -f microblog.db
# Restart backend - it will auto-create new database
```

### Issue: "Connection refused" (Frontend can't reach backend)

**Checklist:**
- [ ] Backend running on http://localhost:8001
- [ ] Frontend proxy configured correctly in `vite.config.js`
- [ ] Both servers are running
- [ ] Check browser console for CORS errors

**Fix:**
```javascript
// vite.config.js
server: {
  port: 3000,
  proxy: {
    '/api': {
      target: 'http://localhost:8001',  // Verify port is 8001
      changeOrigin: true
    }
  }
}
```

### Issue: "Empty feed but I posted"

**Solution**: 
1. Refresh the page (F5 or Cmd+R)
2. Check browser localStorage has token: Open DevTools → Application → localStorage
3. Verify you're logged in (check navbar)

---

## 🧪 Testing

### Backend Tests

```bash
cd backend

# Run all tests
PYTHONPATH=. pytest

# Run specific test file
PYTHONPATH=. pytest tests/test_app.py

# Run with verbose output
PYTHONPATH=. pytest -v

# Run tests with coverage
PYTHONPATH=. pytest --cov=app
```

**Test Coverage:**
- User registration and validation
- Login and JWT authentication
- Post creation and retrieval
- Like functionality (no duplicates)
- Reply functionality
- Profile viewing
- Error handling

### Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run specific test file
npm test Feed.test.jsx

# Run with coverage
npm test -- --coverage

# Exit test mode
# Press 'q' to quit
```

---

## 📊 API Documentation

### Authentication

**Register**
```
POST /api/users/register
Content-Type: application/json

{
  "username": "alice",
  "email": "alice@example.com",
  "password": "password123",
  "bio": "I love coding!"
}

Response: 200
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "bio": "I love coding!"
}
```

**Login**
```
POST /api/users/login
Content-Type: application/json

{
  "username": "alice",
  "password": "password123"
}

Response: 200
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Posts

**Create Post**
```
POST /api/posts/
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "Hello world!",
  "parent_id": null
}

Response: 200
{
  "id": 1,
  "content": "Hello world!",
  "author_id": 1,
  "author_username": "alice",
  "created_at": "2026-01-13T14:00:00",
  "parent_id": null
}
```

**Get Feed**
```
GET /api/posts/feed

Response: 200
[
  {
    "id": 1,
    "content": "Hello world!",
    "author_id": 1,
    "author_username": "alice",
    "created_at": "2026-01-13T14:00:00",
    "parent_id": null
  }
]
```

**Like Post**
```
POST /api/posts/{post_id}/like
Authorization: Bearer <token>

Response: 200
{
  "message": "Post liked"
}
```

**Reply to Post**
```
POST /api/posts/{post_id}/reply
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "Great post!",
  "parent_id": {post_id}
}

Response: 200
{
  "id": 2,
  "content": "Great post!",
  "author_id": 2,
  "author_username": "bob",
  "created_at": "2026-01-13T14:05:00",
  "parent_id": 1
}
```

---

## 🔐 Security Features

1. **Password Hashing**
   - Algorithm: bcrypt
   - Rounds: 12
   - Byte limit: 72 bytes (enforced)

2. **JWT Tokens**
   - Algorithm: HS256
   - Expiration: 60 minutes
   - Storage: Browser localStorage

3. **CORS**
   - Origin: All (configurable)
   - Methods: GET, POST, PUT, DELETE
   - Headers: All standard headers

4. **Input Validation**
   - Username: 3-50 characters
   - Email: Valid format
   - Password: Min 6 characters
   - Post content: Max 280 characters

---

## 📁 File Structure Explained

```
backend/
├── app/main.py
│   ├── Initializes FastAPI app
│   ├── Sets up middleware (CORS, logging)
│   ├── Includes routers with /api prefix
│   └── Creates database tables on startup
│
├── app/routers/
│   ├── users.py → /api/users/ endpoints
│   └── posts.py → /api/posts/ endpoints
│
├── app/services/auth.py
│   ├── Password hashing with bcrypt
│   └── JWT token creation/verification
│
└── logs/app.log.md
    └── All requests/responses logged here

frontend/
├── src/App.jsx
│   ├── Router setup
│   └── Navigation bar
│
├── src/pages/
│   ├── Feed.jsx → Main feed & posting
│   ├── Login.jsx → Authentication
│   ├── Register.jsx → Account creation
│   └── Profile.jsx → User profiles
│
├── src/App.css
│   └── All styling (modern, responsive)
│
└── vite.config.js
    └── API proxy configuration
```

---

## 🎨 UI Color Reference

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | #1da1f2 | Buttons, links, active states |
| Accent Pink | #f91880 | Highlights, gradients |
| Text Primary | #0f1419 | Main text |
| Text Secondary | #536471 | Muted text |
| Border | #eff3f4 | Dividers, subtle borders |
| Background | #f7f9fa | Page background |
| Error | #e7245e | Error messages |
| Success | #17bf63 | Success messages |

---

## 📝 Example Workflows

### Workflow 1: New User Registration & First Post

```
1. User visits http://localhost:3000
2. Clicks "Register"
3. Fills form and creates account
4. Clicks "Sign In" link
5. Enters credentials and logs in
6. Lands on Feed page
7. Types post in text area
8. Clicks "Post"
9. Post appears at top of feed
10. Other users can see it
```

### Workflow 2: Social Interaction

```
1. User sees another user's post
2. Clicks "Like" button
3. Button shows liked status
4. Clicks "Reply" button
5. Types reply (max 280 chars)
6. Clicks "Send"
7. Reply appears below original post
8. Clicks author name to view their profile
9. Sees all their posts and bio
10. Clicks back to feed
```

---

## 🚀 Production Deployment

### Backend (Heroku Example)

```bash
# Install Gunicorn
pip install gunicorn

# Add to requirements.txt
echo "gunicorn" >> requirements.txt

# Create Procfile
echo "web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app" > Procfile

# Deploy
git push heroku main
```

### Frontend (Vercel Example)

```bash
npm run build
# Deploy dist/ folder to Vercel
```

---

## 📞 Support & Debugging

### Check Backend is Running
```bash
curl http://localhost:8001/
# Should return something, not connection error
```

### Check Frontend is Running
```bash
curl http://localhost:3000/
# Should return HTML
```

### View Backend Logs
```bash
tail -f backend/logs/app.log.md
```

### Browser Developer Tools
1. Open DevTools (F12)
2. Check Console tab for JavaScript errors
3. Check Network tab for API requests
4. Check Application → localStorage for JWT token

---

## 📚 References

- **FastAPI**: https://fastapi.tiangolo.com
- **React**: https://react.dev
- **Vite**: https://vitejs.dev
- **SQLAlchemy**: https://www.sqlalchemy.org
- **JWT**: https://jwt.io

---

## ✅ Verification Checklist

Before submission, verify:
- [x] Backend runs on port 8001 without errors
- [x] Frontend runs on port 3000 without errors
- [x] Can register new user
- [x] Can login with credentials
- [x] Can create post (max 280 chars)
- [x] Feed displays all posts
- [x] Can like posts
- [x] Can reply to posts
- [x] Can view user profiles
- [x] Logs are generated in `backend/logs/app.log.md`
- [x] Tests pass with `PYTHONPATH=. pytest`
- [x] UI is responsive and styled
- [x] No console errors in browser

---

**Ready to submit! 🎉**
