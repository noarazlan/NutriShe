from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database import get_db
from data.models.user import User
from utils.security import get_current_user
from data.models.recipe import Recipe
from schemas.recipes_schema import RecipeCardResponse
from data.models.favorite_recipe import FavoriteRecipe

router = APIRouter(prefix="/favorites", tags=["favorites"])

@router.post("/{recipe_id}")
def add_to_favorites(recipe_id : int, current_user: User = Depends(get_current_user), db : Session = Depends(get_db)):

    recipe = db.query(Recipe).filter(Recipe.id == recipe_id, Recipe.is_active.is_(True)).first()
    if recipe is None:
        raise HTTPException(
                            status_code=404,
                            detail="Recipe not found"
                        )
    user_favorite = db.query(FavoriteRecipe).filter(FavoriteRecipe.user_id == current_user.id, FavoriteRecipe.recipe_id == recipe_id).first()
    if user_favorite is not None:
        raise HTTPException(
                    status_code=409,
                    detail="This recipe is already in your favorites"
                )
    
    new_favorite = FavoriteRecipe(user_id = current_user.id ,recipe_id = recipe_id)
    db.add(new_favorite)
    db.commit()
    return {"message" : "Recipe added to favorites successfully"}


@router.delete("/remove-from-favorites/{recipe_id}")
def remove_from_favorites(recipe_id : int , current_user: User = Depends(get_current_user), db : Session = Depends(get_db) ):
    fav = db.query(FavoriteRecipe).filter(FavoriteRecipe.recipe_id == recipe_id, FavoriteRecipe.user_id == current_user.id).first()
    if fav is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe is not in your favorites",
        )
    db.delete(fav)
    db.commit()
    return {"message" : "Recipe removed from favorites successfully"}

@router.get("/", response_model=list[RecipeCardResponse])
def get_favorites(current_user: User = Depends(get_current_user), db : Session = Depends(get_db)):
    fav = db.query(Recipe).join(FavoriteRecipe).filter(FavoriteRecipe.user_id == current_user.id, Recipe.is_active.is_(True)).all()
    return fav
    
    

            