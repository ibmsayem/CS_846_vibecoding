from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import user as user_model, database
from app.schemas import user as user_schema
from app.services import auth
from loguru import logger

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=user_schema.UserOut)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Registration request received for username: {user.username}, email: {user.email}")
    try:
        # Check if user already exists
        db_user = db.query(user_model.User).filter(
            (user_model.User.username == user.username) |
            (user_model.User.email == user.email)
        ).first()
        if db_user:
            logger.warning(f"Registration failed: {user.username} already exists.")
            raise HTTPException(status_code=400, detail="Username or email already registered")
        
        logger.info(f"Hashing password for {user.username}")
        hashed_password = auth.get_password_hash(user.password)
        
        logger.info(f"Creating new user: {user.username}")
        new_user = user_model.User(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password,
            bio=user.bio or ""
        )
        
        logger.info(f"Saving user to database: {user.username}")
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        logger.info(f"User registered successfully: {user.username} (ID: {new_user.id})")
        return new_user
    except HTTPException:
        raise
    except IntegrityError as e:
        db.rollback()
        logger.error(f"IntegrityError during registration for {user.username}: {str(e)}")
        raise HTTPException(status_code=400, detail="Username or email already registered")
    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error during registration for {user.username}: {type(e).__name__}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")

@router.post("/login")
def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        logger.warning(f"Login failed for: {user.username}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = auth.create_access_token({"sub": db_user.username})
    logger.info(f"User logged in: {user.username}")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/{username}", response_model=user_schema.UserOut)
def get_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.username == username).first()
    if not user:
        logger.warning(f"Profile not found: {username}")
        raise HTTPException(status_code=404, detail="User not found")
    return user
@router.put("/{username}", response_model=user_schema.UserOut)
def update_profile(username: str, update_data: user_schema.UserUpdate, db: Session = Depends(get_db), current_user: user_model.User = Depends(auth.get_current_user)):
    # Check if user is updating their own profile
    if current_user.username != username:
        logger.warning(f"Unauthorized profile update attempt by {current_user.username} for {username}")
        raise HTTPException(status_code=403, detail="Cannot update other user's profile")
    
    user = db.query(user_model.User).filter(user_model.User.username == username).first()
    if not user:
        logger.warning(f"Profile not found for update: {username}")
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update allowed fields
    if update_data.bio is not None:
        user.bio = update_data.bio
        logger.info(f"Profile bio updated for {username}")
    
    db.commit()
    db.refresh(user)
    return user