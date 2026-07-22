from sqlalchemy.orm import Session

from data.models.enums import LifeStage, TargetSource
from data.models.reference import NutrientReferenceValue
from data.models.target import UserTarget
from data.models.user import User

from services.nutrition_calculator import (
    calculate_age,
    calculate_daily_calories,
    protein_calculation,
    fats_calculation,
    carbohydrates_calculation,
)


def calculate_and_save_targets(user : User , db : Session):

    weight = float(user.weight_kg)
    height = float(user.height_cm)
    activity_level = user.activity_level.value
    goal = user.goal.value

    calories = calculate_daily_calories(weight=weight, height=height, date_of_birth=user.date_of_birth, activity_level=activity_level, goal=goal)
    protein = protein_calculation(weight=weight, activity_level=activity_level, goal=goal)
    fats = fats_calculation(weight=weight, height=height, date_of_birth=user.date_of_birth, activity_level=activity_level, goal=goal)
    carbs = carbohydrates_calculation(weight=weight, height=height, date_of_birth=user.date_of_birth, activity_level=activity_level,goal=goal)

    user_target = db.query(UserTarget).filter(UserTarget.user_id == user.id).first()

    if user_target is None:
        user_target = UserTarget(user_id = user.id)
        db.add(user_target)

    user_target.calories_target = calories
    user_target.protein_target_g = protein
    user_target.fat_target_g = fats
    user_target.carbohydrates_target_g = carbs
    user_target.target_source = TargetSource.CALCULATED

    age = calculate_age(user.date_of_birth)

    reference_values = (db.query(NutrientReferenceValue).filter(NutrientReferenceValue.min_age <= age, (NutrientReferenceValue.max_age >= age ) | (NutrientReferenceValue.max_age.is_(None)), NutrientReferenceValue.life_stage == LifeStage.STANDARD).all())

    field_mapping = {
    "fiber": "fiber_target_g",
    "iron": "iron_target_mg",
    "calcium": "calcium_target_mg",
    "magnesium": "magnesium_target_mg",
    "potassium": "potassium_target_mg",
    "sodium": "sodium_target_mg",
    "vitamin_a": "vitamin_a_target_mcg",
    "vitamin_c": "vitamin_c_target_mg",
    "vitamin_d": "vitamin_d_target_mcg",
    "vitamin_b12": "vitamin_b12_target_mcg",}

    for reference in reference_values:
        field_name = field_mapping.get(reference.nutrient_code)

        if field_name is not None:
            setattr(
                user_target,
                field_name,
                reference.recommended_amount,
            )

    return user_target

    