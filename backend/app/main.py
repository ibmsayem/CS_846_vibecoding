from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, posts
from app.models import database, user, post
from loguru import logger
import os
from pathlib import Path
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        try:
            body = await request.body()
            logger.info(f"Incoming request: {request.method} {request.url.path} | Body: {body.decode() if body else 'empty'}")
        except:
            logger.info(f"Incoming request: {request.method} {request.url.path}")
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        logger.info(f"Response: {request.method} {request.url.path} | Status: {response.status_code} | Time: {process_time:.3f}s")
        
        return response

app = FastAPI(title="Microblogging App")

# Add middleware
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Logging setup with absolute paths (BEFORE database creation)
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
logger.add(str(log_dir / "app.log.json"), serialize=True, rotation="1 week")
logger.add(str(log_dir / "app.log.md"), format="**{time}** | **{level}** | {message}", rotation="1 week")

@app.on_event("startup")
def startup_event():
    try:
        logger.info("Backend startup: Creating database tables...")
        # Create database tables on startup
        database.Base.metadata.create_all(bind=database.engine)
        logger.info("Database tables created/verified successfully.")
        logger.info("Backend server started and ready to accept requests.")
    except Exception as e:
        logger.error(f"Startup error: {str(e)}")
        raise

# Routers
app.include_router(users.router, prefix="/api")
app.include_router(posts.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Microblogging App API!"}
