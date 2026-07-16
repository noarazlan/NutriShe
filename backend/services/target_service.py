from sqlalchemy.orm import Session
from data.models.enums import TargetSource
from data.models.target import UserTarget
from data.models.user import User
from services.nutrition_calculator import (
    calculate_daily_calories,
    protein_calculation,
    fats_calculation,
    carbohydrates_calculation,
)

def calculate_and_save_targets(user : User, db : Session):

    activity_level = user.activity_level.value
    goal = user.goal.value
    weight = float(user.weight_kg)
    height = float(user.height_cm)

    calories = calculate_daily_calories(weight=weight, height=height, date_of_birth=user.date_of_birth, 
                                        activity_level=activity_level, goal=goal)
    
    protein = protein_calculation(weight=weight, activity_level=activity_level, goal=goal)

    fats = fats_calculation(weight=weight, height=height, date_of_birth=user.date_of_birth, 
                            activity_level=activity_level, goal=goal)
    
    carbs = carbohydrates_calculation(weight=weight, height=height, date_of_birth=user.date_of_birth, 
                                     activity_level=activity_level, goal=goal)
    
    