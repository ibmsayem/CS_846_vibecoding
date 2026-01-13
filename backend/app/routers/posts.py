from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import post as post_model, user as user_model, database
from app.schemas import post as post_schema
from app.services import auth
from loguru import logger
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=post_schema.PostOut)
def create_post(post: post_schema.PostCreate, db: Session = Depends(get_db), current_user: user_model.User = Depends(auth.get_current_user)):
    if len(post.content) > 280:
        logger.warning(f"Post too long by user {current_user.username}")
        raise HTTPException(status_code=400, detail="Post exceeds 280 characters")
    new_post = post_model.Post(
        content=post.content,
        author_id=current_user.id,
        parent_id=post.parent_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    new_post.author_username = current_user.username
    new_post.like_count = 0
    logger.info(f"Post created by {current_user.username}: {new_post.id}")
    return new_post

@router.get("/feed", response_model=List[post_schema.PostOut])
def get_feed(db: Session = Depends(get_db)):
    # Only return posts that are NOT replies (parent_id is None)
    posts = db.query(post_model.Post).filter(post_model.Post.parent_id == None).order_by(post_model.Post.created_at.desc()).all()
    # Add author_username and like_count to each post
    for post in posts:
        if post.author:
            post.author_username = post.author.username
        post.like_count = db.query(post_model.Like).filter(post_model.Like.post_id == post.id).count()
    return posts

@router.get("/{post_id}/replies", response_model=List[post_schema.PostOut])
def get_replies(post_id: int, db: Session = Depends(get_db)):
    # Get all replies for a specific post
    replies = db.query(post_model.Post).filter(post_model.Post.parent_id == post_id).order_by(post_model.Post.created_at.asc()).all()
    # Add author_username and like_count to each reply
    for reply in replies:
        if reply.author:
            reply.author_username = reply.author.username
        reply.like_count = db.query(post_model.Like).filter(post_model.Like.post_id == reply.id).count()
    return replies

@router.post("/{post_id}/like")
def like_post(post_id: int, db: Session = Depends(get_db), current_user: user_model.User = Depends(auth.get_current_user)):
    post = db.query(post_model.Post).filter(post_model.Post.id == post_id).first()
    if not post:
        logger.warning(f"Like failed: Post {post_id} not found")
        raise HTTPException(status_code=404, detail="Post not found")
    like = db.query(post_model.Like).filter_by(user_id=current_user.id, post_id=post_id).first()
    if like:
        logger.warning(f"User {current_user.username} already liked post {post_id}")
        raise HTTPException(status_code=400, detail="Already liked")
    new_like = post_model.Like(user_id=current_user.id, post_id=post_id)
    db.add(new_like)
    db.commit()
    logger.info(f"User {current_user.username} liked post {post_id}")
    return {"message": "Post liked"}

@router.post("/{post_id}/reply", response_model=post_schema.PostOut)
def reply_post(post_id: int, post: post_schema.PostCreate, db: Session = Depends(get_db), current_user: user_model.User = Depends(auth.get_current_user)):
    parent_post = db.query(post_model.Post).filter(post_model.Post.id == post_id).first()
    if not parent_post:
        logger.warning(f"Reply failed: Parent post {post_id} not found")
        raise HTTPException(status_code=404, detail="Parent post not found")
    if post.parent_id and post.parent_id != post_id:
        logger.warning(f"Reply failed: Invalid parent_id {post.parent_id}")
        raise HTTPException(status_code=400, detail="Invalid parent_id")
    new_post = post_model.Post(
        content=post.content,
        author_id=current_user.id,
        parent_id=post_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    new_post.author_username = current_user.username
    new_post.like_count = 0
    logger.info(f"User {current_user.username} replied to post {post_id}")
    return new_post

@router.get("/user/{username}", response_model=List[post_schema.PostOut])
def get_user_posts(username: str, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.username == username).first()
    if not user:
        logger.warning(f"User posts not found: {username}")
        raise HTTPException(status_code=404, detail="User not found")
    posts = db.query(post_model.Post).filter(post_model.Post.author_id == user.id).order_by(post_model.Post.created_at.desc()).all()
    # Add author_username and like_count to each post
    for post in posts:
        if post.author:
            post.author_username = post.author.username
        post.like_count = db.query(post_model.Like).filter(post_model.Like.post_id == post.id).count()
    return posts
