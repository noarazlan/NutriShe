import os
from datetime import datetime, timedelta, timezone
from typing import Any
import bcrypt
import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from data.database import get_db
from data.models.user import User

# Load environment variables from the .env file
load_dotenv()

# JWT Configuration settings
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "SUPER_SECRET_KEY_CHANGE_ME")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  

# Defines where FastAPI should look for the token (the login endpoint)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


def hash_password(password: str) -> str:
    """Hash a plain text password using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain text password against the stored hash."""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )


def create_access_token(data: dict[str, Any]) -> str:
    """Create a secure JWT access token for an authenticated user."""
    to_encode = data.copy()
    # Set the expiration timestamp for the token
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    # Encode the payload into a JWT string using the secret key
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",
                                            headers={"WWW-Authenticate": "Bearer"},)

    try:
        # Decode the incoming JWT token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extract the user ID  
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        
        user_id = int(user_id)
        
    except (InvalidTokenError, ValueError, TypeError):
        # Catch token errors or type parsing errors
        raise credentials_exception
    # Query the database to find the user matching the ID from the token
    user = (db.query(User).filter(User.id == user_id).first())
    if user is None:
        raise credentials_exception
    
    return user
        