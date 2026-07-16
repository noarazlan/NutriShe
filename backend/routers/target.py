from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
from data.models.user import User
from utils.security import get_current_user
from data.models.target import UserTarget


router = APIRouter(prefix="/target", tags=["target"])

@router.get("/me") 
def get_my_target(current_user : User = Depends(get_current_user), db : Session = Depends(get_db)):

    user_target = db.query(UserTarget).filter(UserTarget.id == current_user.id).first()

    if user_target is None:
        return {"message" : "Targets have not been calculated yet"}
    
    return {
        "calories": user_target.calories_target,
        "protein_g": user_target.protein_target_g,
        "fat_g": user_target.fat_target_g,
        "carbohydrates_g": user_target.carbohydrates_target_g,
        "fiber_g": user_target.fiber_target_g,
        "iron_mg": user_target.iron_target_mg,
        "calcium_mg": user_target.calcium_target_mg,
        "magnesium_mg": user_target.magnesium_target_mg,
        "potassium_mg": user_target.potassium_target_mg,
        "sodium_mg": user_target.sodium_target_mg,
        "vitamin_a_mcg": user_target.vitamin_a_target_mcg,
        "vitamin_c_mg": user_target.vitamin_c_target_mg,
        "vitamin_d_mcg": user_target.vitamin_d_target_mcg,
        "vitamin_b12_mcg": user_target.vitamin_b12_target_mcg,
        "folate_mcg": user_target.folate_target_mcg,
        "target_source": user_target.target_source,
        "calculation_method": user_target.calculation_method,
        "updated_at": user_target.updated_at,
    }
