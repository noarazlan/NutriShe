from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from data.database import get_db
from data.models.food import Food, FoodCategory
from data.models.enums import FoodCategoryType
from data.models.user import User
from data.models.reference import NutrientReferenceValue
from schemas.food_schema import FoodResponse
from utils.security import get_current_user

router = APIRouter(prefix="/foods", tags=["foods"])


@router.get("/category/{category_name}", response_model=list[FoodResponse])
def get_foods_by_category(
    category_name: FoodCategoryType, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Fetch and automatically filter foods based on the current user's diet preferences.
    """
    # 1. Fetch all foods belonging to this category
    all_foods = (
        db.query(Food)
        .join(FoodCategory)
        .filter(FoodCategory.category == category_name)
        .all()
    )

    # 2. Get the preference codes of the current user
    user_pref_codes = [up.preference.code for up in current_user.preferences]

    filtered_foods = []
    
    for food in all_foods:
        food_pref_codes = [fp.preference.code for fp in food.preferences]

        # Filter out non-vegetarian foods for Vegetarian users
        if "vegetarian" in user_pref_codes:
            if "vegetarian" not in food_pref_codes and "vegan" not in food_pref_codes:
                continue

        # Filter out non-vegan foods for Vegan users
        if "vegan" in user_pref_codes:
            if "vegan" not in food_pref_codes:
                continue

        # Filter out foods containing gluten for Gluten Free users
        if "gluten_free" in user_pref_codes:
            if "gluten_free" not in food_pref_codes:
                continue

        # Filter out foods containing lactose for Lactose Free users
        if "lactose_free" in user_pref_codes:
            if "lactose_free" not in food_pref_codes:
                continue

        filtered_foods.append(food)

    return filtered_foods


@router.get("/reference/{nutrient_code}")
def get_nutrient_reference_value(
    nutrient_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get the recommended daily nutrient reference value based on the user's age group.
    """
    # Calculate age from date_of_birth
    today = date.today()
    birth = current_user.date_of_birth
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    # Query the reference value from nutrient_reference_values table
    ref_value = (
        db.query(NutrientReferenceValue)
        .filter(
            NutrientReferenceValue.nutrient_code == nutrient_code,
            NutrientReferenceValue.min_age <= age,
            (NutrientReferenceValue.max_age >= age) | (NutrientReferenceValue.max_age == None)
        )
        .first()
    )

    if not ref_value:
        return {"nutrient_code": nutrient_code, "recommended_amount": 0, "unit": "g"}

    return {
        "nutrient_code": ref_value.nutrient_code,
        "recommended_amount": ref_value.recommended_amount,
        "unit": ref_value.unit
    }
