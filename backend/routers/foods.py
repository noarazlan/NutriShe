from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.database import get_db
from data.models.food import Food, FoodCategory
from data.models.enums import FoodCategoryType
from schemas.food_schema import FoodResponse

router = APIRouter(prefix="/foods", tags=["foods"])


@router.get("/category/{category_name}", response_model=list[FoodResponse])
def get_foods_by_category(
    category_name: FoodCategoryType, db: Session = Depends(get_db)
):
    """
    Fetch all foods belonging to a specific category (e.g., protein, carbohydrates, fat, fiber).
    """
    foods = (
        db.query(Food)
        .join(FoodCategory)
        .filter(FoodCategory.category == category_name)
        .all()
    )
    return foods