from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database import get_db
from data.models.user import User
from utils.security import get_current_user
from data.models.recipe import Recipe, RecipeMealType
from schemas.recipes_schema import RecipeCardResponse, RecipeDetailsResponse
from data.models.enums import MealType

router = APIRouter(prefix="/recipes", tags=["recipes"])

@router.get("/", response_model=list[RecipeCardResponse])
def get_recipes(db : Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    user_preferences_codes = {user_preference.preference.code
                              for user_preference in current_user.preferences}
    all_recipes = db.query(Recipe).filter(Recipe.is_active.is_(True)).all()

    matching_recipes = []
    for recipe in all_recipes:
        recipe_preferences_codes = {recipe_preference.preference.code
                                    for recipe_preference in recipe.preferences }

        if user_preferences_codes.issubset(recipe_preferences_codes):
            matching_recipes.append(recipe)

    return matching_recipes


@router.get("/all-recipes", response_model=list[RecipeCardResponse])
def get_all_recipes(db : Session = Depends(get_db)):
    all_recipes = db.query(Recipe).filter(Recipe.is_active.is_(True)).all()
    return all_recipes


@router.get("/meal-type/{meal_type}", response_model=list[RecipeCardResponse])
def get_recipes_by_meal_types(meal_type : MealType, db : Session = Depends(get_db)):
    meal_type_recipes = db.query(Recipe).join(RecipeMealType).filter(RecipeMealType.meal_type==meal_type,
                                                                     Recipe.is_active.is_(True)).all()
    return meal_type_recipes

@router.get("/{recipe_id}", response_model=RecipeDetailsResponse)
def get_recipe_by_id( recipe_id : int ,db : Session = Depends(get_db)):
    recipe =  db.query(Recipe).filter(Recipe.id == recipe_id, Recipe.is_active.is_(True)
).first()
    if recipe is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )
    return recipe


