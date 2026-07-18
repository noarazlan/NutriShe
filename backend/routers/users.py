from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from data.database import get_db
from data.models.user import User
from data.models.preference import UserPreference
from schemas.user_schema import UserRegister, UserLogin, Token, UserResponse
from utils.security import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserResponse)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    # 1. Check if the email already exists
    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # 2. Check if the username is already taken
    existing_username = db.query(User).filter(User.username == user_data.username).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken",
        )

    # 3. Hash password and create the new user
    hashed_pw = hash_password(user_data.password)
    new_user = User(
        full_name=user_data.full_name,
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_pw,
        date_of_birth=user_data.date_of_birth,
        weight_kg=user_data.weight_kg,
        height_cm=user_data.height_cm,
        activity_level=user_data.activity_level,
        goal=user_data.goal,
    )
    
    db.add(new_user)
    db.flush()  # Generate user ID for preference mapping

    # 4. Save diet and health preferences from onboarding
    for pref_id in user_data.preference_ids:
        user_pref = UserPreference(user_id=new_user.id, preference_id=pref_id)
        db.add(user_pref)

    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    # Authenticate user using username
    user = db.query(User).filter(User.username == login_data.username).first()
    
    if not user or not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    # Generate the access token
    token_data = {"sub": str(user.id), "username": user.username}
    token = create_access_token(token_data)

    return {"access_token": token, "token_type": "bearer"}


# Optional: Endpoint to get the logged-in user profile details
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user