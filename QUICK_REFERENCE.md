# 🎯 VibeCode Quick Reference Card

## 🚀 Quick Start (2 minutes)

### Terminal 1: Backend
```bash
cd backend
source venv/bin/activate
PYTHONPATH=. uvicorn app.main:app --reload --port 8001
```

### Terminal 2: Frontend
```bash
cd frontend
npm run dev
```

### Browser
```
http://localhost:3000
```

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| README.md | Project overview |
| SETUP_GUIDE.md | Detailed installation & troubleshooting |
| API_DOCS.md | API endpoint reference |
| PROJECT_SUMMARY.md | Architecture & implementation details |

---

## 👤 Test Accounts

### Account 1
- **Username**: alice
- **Email**: alice@example.com
- **Password**: password123

### Account 2
- **Username**: bob
- **Email**: bob@example.com
- **Password**: secret456

---

## 🎮 Quick Test (5 minutes)

1. **Register** → Click Register button, fill form, submit
2. **Login** → Use test account credentials
3. **Post** → Type "Hello World!", click Post
4. **Like** → Click ❤️ Like on any post
5. **Reply** → Click 💬 Reply, type message, send
6. **Profile** → Click username to view profile

---

## 🔧 Key Ports

| Service | Port | URL |
|---------|------|-----|
| Backend | 8001 | http://localhost:8001 |
| Frontend | 3000 | http://localhost:3000 |

---

## 🌐 Key API Endpoints

```
POST   /api/users/register       Register new user
POST   /api/users/login          Login & get JWT token
GET    /api/users/{username}     Get user profile

POST   /api/posts/               Create post
GET    /api/posts/feed           Get all posts
GET    /api/posts/user/{user}    Get user's posts
POST   /api/posts/{id}/like      Like a post
POST   /api/posts/{id}/reply     Reply to post
```

---

## 🎨 Design Colors

- **Primary**: #1da1f2 (Blue)
- **Accent**: #f91880 (Pink)
- **Text**: #0f1419 (Dark)
- **Border**: #eff3f4 (Light)

---

## ⚙️ Important File Locations

```
backend/
  ├── app/main.py               ← FastAPI app
  ├── app/models/               ← Database models
  ├── app/routers/              ← API endpoints
  ├── logs/app.log.md           ← Logs
  └── microblog.db              ← Database

frontend/
  ├── src/App.jsx               ← Main component
  ├── src/pages/                ← Pages (Feed, Login, etc)
  ├── src/App.css               ← Styles
  └── vite.config.js            ← Vite config
```

---

## 🆘 Troubleshooting Cheat Sheet

| Problem | Solution |
|---------|----------|
| Port in use | `lsof -i :PORT \| tail -n +2 \| awk '{print $2}' \| xargs kill -9` |
| Module error | Activate venv: `source venv/bin/activate` |
| DB locked | Delete `microblog.db`, restart backend |
| Can't post | Check login status, verify token in localStorage |
| Empty feed | Refresh page, check browser console |
| CORS error | Ensure backend on 8001, frontend on 3000 |

---

## 📋 Constraints & Limits

| Feature | Limit |
|---------|-------|
| Post length | 280 characters |
| Username length | 3-50 characters |
| Bio length | 160 characters |
| Password length | 6-72 characters |
| Token expiration | 60 minutes |
| Post level | Replies only 1 level deep |

---

## ✨ Features

✅ User registration & login
✅ Create posts (280 chars)
✅ Global feed
✅ Like posts
✅ Reply to posts
✅ User profiles
✅ Secure authentication (JWT)
✅ Password hashing (bcrypt)
✅ Request logging
✅ Modern responsive UI

---

## 🧪 Testing Commands

```bash
# Backend tests
cd backend
PYTHONPATH=. pytest

# Frontend tests
cd frontend
npm test

# Check endpoints
curl http://localhost:8001/api/posts/feed
```

---

## 📱 Browser DevTools Tips

1. **Check Token**: DevTools → Application → localStorage → token
2. **View Logs**: DevTools → Console tab
3. **Network Requests**: DevTools → Network tab
4. **Clear Cache**: Ctrl+Shift+Del → Clear all

---

## 🔐 Security Reminders

- ✅ Passwords bcrypt hashed (12 rounds)
- ✅ JWT tokens with 60-minute expiration
- ✅ Input validation on all endpoints
- ✅ CORS enabled for frontend
- ✅ Password limit: 72 bytes (bcrypt constraint)

---

## 📊 Project Stats

- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: React 18, Vite, CSS3
- **Total Files**: 30+
- **Total LOC**: 2000+
- **Test Coverage**: Core features
- **Documentation**: 1000+ lines

---

## 🎓 Course Info

- **Course**: CS 846
- **Student**: Ibrahim Sayem
- **Date**: January 13, 2026
- **Status**: ✅ Complete

---

## 📞 Quick Help

1. **Setup issues?** → See SETUP_GUIDE.md
2. **API questions?** → See API_DOCS.md
3. **Architecture?** → See PROJECT_SUMMARY.md
4. **General info?** → See README.md

---

## ✅ Pre-Submission Checklist

- [ ] Backend running on 8001 without errors
- [ ] Frontend running on 3000 without errors
- [ ] Can register new user
- [ ] Can login with credentials
- [ ] Can create posts
- [ ] Can like posts
- [ ] Can reply to posts
- [ ] Can view profiles
- [ ] Logs generating
- [ ] Tests passing
- [ ] No console errors
- [ ] Documentation complete

---

**Ready to submit! 🎉**

For detailed help, see the full documentation files.
