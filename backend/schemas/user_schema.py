from datetime import date
from decimal import Decimal
from pydantic import BaseModel, EmailStr
from data.models.enums import ActivityLevel, UserGoal


class UserRegister(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    password: str  
    date_of_birth: date
    weight_kg: Decimal
    height_cm: Decimal
    activity_level: ActivityLevel
    goal: UserGoal
    preference_ids: list[int] = []  


class UserLogin(BaseModel):
    username: str 
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True