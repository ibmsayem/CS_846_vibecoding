
# 🚀 VibeCode - CS846 Microblogging Application

A modern, full-stack Twitter-like microblogging application built with **FastAPI** (Backend) and **React** (Frontend). Users can register, login, create posts, like posts, and reply to posts with a beautiful, interactive UI.

## ✨ Features

### User Management
- ✅ User Registration with email validation
- ✅ JWT-based Authentication (60-minute token expiration)
- ✅ Secure password hashing with bcrypt (12 rounds, 72-byte limit)
- ✅ User profiles with bio
- ✅ Profile viewing for other users

### Posting & Interactions
- ✅ Create posts (max 280 characters)
- ✅ Global feed with posts from all users
- ✅ Like functionality with duplicate prevention
- ✅ Reply to posts (one level deep)
- ✅ View posts by specific users

### Technical Features
- ✅ Request/Response logging with loguru (JSON + Markdown formats)
- ✅ CORS enabled for frontend-backend communication
- ✅ SQLAlchemy ORM with SQLite database
- ✅ Comprehensive error handling
- ✅ Responsive, modern UI design
- ✅ Real-time feed updates
- ✅ Automated tests (backend and frontend)

---

## 📋 Project Structure

```
CS_846_vibecoding/
├── backend/
│   ├── app/
│   │   ├── main.py                 # FastAPI application entry point
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── database.py         # SQLAlchemy configuration
│   │   │   ├── user.py             # User ORM model
│   │   │   └── post.py             # Post & Like ORM models
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── users.py            # User endpoints (register, login, profile)
│   │   │   └── posts.py            # Post endpoints (CRUD, like, reply)
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py             # Pydantic request/response models
│   │   │   └── post.py             # Pydantic post models
│   │   └── services/
│   │       ├── __init__.py
│   │       └── auth.py             # Password hashing & JWT tokens
│   ├── logs/
│   │   └── app.log.md              # Application logs
│   ├── requirements.txt            # Python dependencies
│   └── venv/                       # Virtual environment
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Feed.jsx            # Global feed & post creation
│   │   │   ├── Login.jsx           # Login form
│   │   │   ├── Register.jsx        # Registration form
│   │   │   └── Profile.jsx         # User profile page
│   │   ├── App.jsx                 # Main app with routing
│   │   ├── App.css                 # Main stylesheet
│   │   ├── index.css               # Global styles
│   │   └── main.jsx                # React entry point
│   ├── public/
│   ├── vite.config.js              # Vite config with API proxy
│   ├── package.json                # Node dependencies
│   └── dist/                       # Production build
│
└── README.md                       # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 16+
- npm or yarn

### Backend Setup
```bash
cd backend

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend (port 8001)
PYTHONPATH=. uvicorn app.main:app --reload --port 8001
```

### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Run frontend (port 3000)
npm run dev
```

### Open in Browser
```
http://localhost:3000
```

---

## 📡 API Endpoints

### User Endpoints (`/api/users/`)
- `POST /register` - Register new user
- `POST /login` - Login user (returns JWT token)
- `GET /{username}` - Get user profile

### Post Endpoints (`/api/posts/`)
- `POST /` - Create post (requires auth)
- `GET /feed` - Get global feed
- `GET /user/{username}` - Get user's posts
- `POST /{post_id}/like` - Like a post (requires auth)
- `POST /{post_id}/reply` - Reply to post (requires auth)

---

## 🔐 Authentication

- **Registration**: Create account with username, email, password
- **Login**: Returns JWT token valid for 60 minutes
- **Protected Routes**: Token sent as `Authorization: Bearer <token>`
- **Password Security**: Bcrypt hashing with 12 rounds

---

## 🎨 Design Features

### Color Scheme
- Primary Blue: `#1da1f2`
- Accent Pink: `#f91880`
- Clean white backgrounds with subtle borders
- Professional typography

### Interactive Elements
- Smooth hover transitions
- Focus states with blue glow
- Error/success messages with icons
- Loading states on buttons
- Fully responsive (mobile/tablet/desktop)

---

## 🧪 Testing

### Backend Tests
```bash
cd backend
PYTHONPATH=. pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

---

## 📝 Logging

All requests and responses logged to `backend/logs/app.log.md`:
- Timestamp
- Request method and path
- Request body
- Response status code
- Response time
- Error details

---

## 🛠️ Tech Stack

**Backend**: FastAPI, SQLAlchemy, SQLite, PyJWT, bcrypt, loguru
**Frontend**: React 18, Vite, axios, react-router-dom
**Database**: SQLite with ORM relationships

---

## 🚀 Deployment

### Backend
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

### Frontend
```bash
npm run build  # Creates dist/ folder
# Deploy dist/ to Vercel, Netlify, etc.
```

---

## 📚 Database Schema

**Users**: id, username (unique), email (unique), hashed_password, bio, created_at
**Posts**: id, content (max 280 chars), author_id, parent_id (for replies), created_at
**Likes**: id, user_id, post_id, created_at (unique constraint on user_id + post_id)

---

## ✅ Features Checklist

- [x] User Registration with validation
- [x] JWT-based Login/Authentication
- [x] Create Posts (280 character limit)
- [x] Global Feed
- [x] Like Posts
- [x] Reply to Posts
- [x] User Profiles
- [x] Secure Password Hashing
- [x] Request/Response Logging
- [x] CORS Configuration
- [x] Modern UI Design
- [x] Responsive Layout
- [x] Error Handling
- [x] Database ORM
- [x] Automated Tests

---

## 👨‍💻 Author

**Student**: Ibrahim Sayem
**Course**: CS 846
**Date**: January 13, 2026

---

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Port already in use | Kill process or use different port (e.g., `--port 8002`) |
| Database locked | Delete `backend/microblog.db` and restart |
| Module not found | Activate virtual environment and install dependencies |
| CORS errors | Ensure backend on 8001, frontend on 3000 |
| Frontend can't connect to API | Check vite.config.js proxy configuration |

---

**Happy Coding! 🎉**
