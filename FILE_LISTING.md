# 📋 Complete Project File Listing

## 📂 Root Directory Files
```
CS_846_vibecoding/
├── README.md                  Main project overview
├── SETUP_GUIDE.md             Step-by-step installation guide
├── API_DOCS.md                Complete API reference
├── PROJECT_SUMMARY.md         Architecture & implementation details
├── QUICK_REFERENCE.md         Quick start cheat sheet
└── FILE_LISTING.md            This file
```

---

## 🔧 Backend Directory (`backend/`)

### Configuration Files
```
backend/
├── requirements.txt           Python package dependencies
├── init_db.py                 Database initialization script
├── .gitignore                 Git ignore file
└── venv/                      Virtual environment (if created)
```

### Application Code (`app/`)
```
backend/app/
├── __init__.py                Package initialization
├── main.py                    FastAPI application entry point
│                             - CORS middleware setup
│                             - Request logging middleware
│                             - Router includes with /api prefix
│                             - Startup event for DB creation
│
├── models/                    Database models
│   ├── __init__.py
│   ├── database.py            SQLAlchemy setup
│   │                         - Engine configuration
│   │                         - SessionLocal factory
│   │                         - Base class for models
│   ├── user.py                User model
│   │                         - username (unique)
│   │                         - email (unique)
│   │                         - hashed_password
│   │                         - bio
│   │                         - Relationships to posts/likes
│   └── post.py                Post & Like models
│                             - Post: content, author, parent_id
│                             - Like: user_id, post_id (unique)
│                             - Relationships defined
│
├── routers/                   API route handlers
│   ├── __init__.py
│   ├── users.py               User endpoints
│   │                         - POST /register
│   │                         - POST /login
│   │                         - GET /{username}
│   └── posts.py               Post endpoints
│                             - POST / (create)
│                             - GET /feed
│                             - GET /user/{username}
│                             - POST /{id}/like
│                             - POST /{id}/reply
│
├── schemas/                   Pydantic models (validation)
│   ├── __init__.py
│   ├── user.py                User schemas
│   │                         - UserCreate (registration)
│   │                         - UserLogin (authentication)
│   │                         - UserOut (response)
│   └── post.py                Post schemas
│                             - PostCreate (creation)
│                             - PostOut (response)
│                             - LikeOut (response)
│
├── services/                  Business logic
│   ├── __init__.py
│   └── auth.py                Authentication service
│                             - get_password_hash()
│                             - verify_password()
│                             - create_access_token()
│                             - get_current_user()
│                             - get_db() dependency
│
└── logs/                      Application logs
    └── app.log.md             Request/response logs (auto-generated)
                              - Markdown format
                              - Timestamps
                              - Request/response details
                              - Errors and exceptions
```

### Database
```
backend/
└── microblog.db              SQLite database file (auto-created)
                              - users table
                              - posts table
                              - likes table
                              - Indexes on foreign keys
```

---

## 💻 Frontend Directory (`frontend/`)

### Configuration Files
```
frontend/
├── vite.config.js            Vite bundler configuration
│                            - React plugin
│                            - Dev server on port 3000
│                            - API proxy to /api → localhost:8001
├── package.json              Node package configuration
│                            - Scripts (dev, build, preview, test)
│                            - Dependencies (react, vite, axios, etc)
├── .gitignore                Git ignore file
└── node_modules/             Installed npm packages (if npm install run)
```

### Source Code (`src/`)
```
frontend/src/
├── __init__.py               Package marker
├── main.jsx                  React entry point
│                            - Import App component
│                            - Mount to #root
│                            - Import global CSS
│
├── App.jsx                   Main application component
│                            - Router setup (BrowserRouter)
│                            - Navigation bar component
│                            - Route definitions
│                            - Token parsing from localStorage
│
├── App.css                   Main stylesheet
│                            - CSS variables (colors)
│                            - Navbar styles
│                            - Form styles
│                            - Feed & post styles
│                            - Profile styles
│                            - Responsive breakpoints
│
├── index.css                 Global CSS
│                            - Reset styles
│                            - Body styles
│                            - Scrollbar styling
│                            - Selection styles
│
├── pages/                    Page components
│   ├── Feed.jsx              Global feed page
│   │                        - Post creation form
│   │                        - Feed display
│   │                        - Like functionality
│   │                        - Reply functionality
│   │                        - Character counter
│   │
│   ├── Login.jsx             Login page
│   │                        - Username/password form
│   │                        - JWT token handling
│   │                        - Error display
│   │                        - Redirect to feed
│   │
│   ├── Register.jsx          Registration page
│   │                        - Username validation
│   │                        - Email validation
│   │                        - Password validation
│   │                        - Bio field (optional)
│   │                        - Redirect to login
│   │
│   └── Profile.jsx           User profile page
│                            - Display user bio
│                            - User's posts
│                            - Post count stat
│                            - Loading state
│
└── __tests__/                Test files
    ├── Feed.test.jsx         Feed component tests
    ├── Login.test.jsx        Login component tests
    ├── Register.test.jsx     Register component tests
    └── Profile.test.jsx      Profile component tests
```

### Build Artifacts
```
frontend/
├── dist/                     Production build (after npm run build)
│   ├── index.html
│   ├── assets/              JavaScript bundles
│   └── assets/              CSS files
└── public/                   Static files
    ├── index.html            HTML template
    └── favicon.ico           (if present)
```

---

## 📊 Database Tables

### Users Table
```
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    bio TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Posts Table
```
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(280) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    author_id INTEGER NOT NULL FOREIGN KEY REFERENCES users(id),
    parent_id INTEGER FOREIGN KEY REFERENCES posts(id)
);
```

### Likes Table
```
CREATE TABLE likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL FOREIGN KEY REFERENCES users(id),
    post_id INTEGER NOT NULL FOREIGN KEY REFERENCES posts(id),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, post_id)
);
```

---

## 📦 Dependencies

### Backend (`requirements.txt`)
```
fastapi           # REST API framework
uvicorn           # ASGI server
sqlalchemy        # ORM
pydantic          # Data validation
python-jose       # JWT handling
passlib[bcrypt]   # Password hashing
bcrypt            # Bcrypt library
python-multipart  # Form data parsing
loguru            # Logging
email-validator   # Email validation
```

### Frontend (`package.json`)
```
"react"                 # UI framework
"react-dom"             # React rendering
"react-router-dom"      # Client-side routing
"axios"                 # HTTP client
"vite"                  # Bundler
"@vitejs/plugin-react"  # React Vite plugin
"@testing-library/react" # Testing utilities
```

---

## 🔄 File Relationships

### Frontend to Backend
```
Feed.jsx
  ├── axios.get('/api/posts/feed')       → posts.py: get_feed()
  ├── axios.post('/api/posts/')          → posts.py: create_post()
  ├── axios.post('/api/posts/{id}/like')  → posts.py: like_post()
  └── axios.post('/api/posts/{id}/reply') → posts.py: reply_post()

Login.jsx
  └── axios.post('/api/users/login')      → users.py: login()

Register.jsx
  └── axios.post('/api/users/register')   → users.py: register()

Profile.jsx
  ├── axios.get('/api/users/{username}')  → users.py: get_profile()
  └── axios.get('/api/posts/user/{user}')  → posts.py: get_user_posts()
```

### Database Relationships
```
User (1) ──────────→ (Many) Post
      └─ posts
      └─ likes

Post (1) ──────────→ (Many) Like
     ├─ author (FK to User)
     ├─ parent (FK to Post)
     ├─ replies
     └─ likes

Like (Many) ───→ (1) User
       └─ user
       └─ post
```

---

## 🔐 Authentication Flow Files

```
register.jsx → POST /api/users/register
                ↓
             users.py register()
                ↓
             auth.py get_password_hash()
                ↓
             Save to database

login.jsx → POST /api/users/login
             ↓
          users.py login()
             ↓
          auth.py verify_password()
             ↓
          auth.py create_access_token()
             ↓
          Return JWT token
             ↓
          Store in localStorage
             ↓
          Include in future requests
```

---

## 📝 Logging Flow

```
main.py RequestLoggingMiddleware
    ↓
Log incoming request (method, path, body)
    ↓
Process request through routers
    ↓
Log outgoing response (status, time)
    ↓
loguru writes to logs/app.log.md
    ↓
Markdown formatted with timestamps
```

---

## 🧪 Test Files Location

```
Backend Tests (if present):
  backend/tests/
    ├── test_app.py           # Main test file
    ├── test_users.py         # User endpoint tests
    └── test_posts.py         # Post endpoint tests

Frontend Tests:
  frontend/src/__tests__/
    ├── Feed.test.jsx
    ├── Login.test.jsx
    ├── Register.test.jsx
    └── Profile.test.jsx
```

---

## 📊 File Statistics

| Category | Count | Files |
|----------|-------|-------|
| Documentation | 6 | README, SETUP_GUIDE, API_DOCS, etc |
| Backend Code | 12 | main.py, models, routers, schemas, services |
| Frontend Code | 8 | App.jsx, pages, CSS files |
| Configuration | 4 | vite.config.js, requirements.txt, package.json |
| Database | 1 | microblog.db |
| Logs | 1 | app.log.md |
| **Total** | **32** | **All files combined** |

---

## 🔍 How to Find What You Need

| Looking for... | Check file... |
|---|---|
| User registration logic | `backend/app/routers/users.py` |
| Password hashing | `backend/app/services/auth.py` |
| Database models | `backend/app/models/post.py` & `user.py` |
| Post creation | `backend/app/routers/posts.py` |
| Frontend form | `frontend/src/pages/Register.jsx` |
| Styling | `frontend/src/App.css` |
| Setup instructions | `SETUP_GUIDE.md` |
| API reference | `API_DOCS.md` |
| Architecture | `PROJECT_SUMMARY.md` |
| Quick help | `QUICK_REFERENCE.md` |

---

## ✅ Verification Checklist

All files present:
- [x] README.md
- [x] SETUP_GUIDE.md
- [x] API_DOCS.md
- [x] PROJECT_SUMMARY.md
- [x] QUICK_REFERENCE.md
- [x] FILE_LISTING.md (this file)
- [x] backend/ directory with all code
- [x] frontend/ directory with all code
- [x] logs/app.log.md in backend
- [x] requirements.txt in backend
- [x] package.json in frontend
- [x] All Python and React files

---

**Last Updated**: January 13, 2026
**Status**: Complete ✅
**Ready for Submission**: Yes ✅
