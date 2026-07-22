from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from data.database import get_db
from data.models.user import User
from utils.security import get_current_user
from data.models.target import UserTarget
from services.target_service import calculate_and_save_targets
from schemas.target_schema import TargetResponse


router = APIRouter(prefix="/target", tags=["target"])

def build_target_response(user_target : UserTarget, user : User):
    return {
        "full_name" : user.full_name,
        "calories": user_target.calories_target,
        "protein": user_target.protein_target_g,
        "fat": user_target.fat_target_g,
        "carbohydrates": user_target.carbohydrates_target_g,
        "fiber": user_target.fiber_target_g,
        "iron": user_target.iron_target_mg,
        "calcium": user_target.calcium_target_mg,
        "magnesium": user_target.magnesium_target_mg,
        "potassium": user_target.potassium_target_mg,
        "sodium": user_target.sodium_target_mg,
        "vitamin_a": user_target.vitamin_a_target_mcg,
        "vitamin_c": user_target.vitamin_c_target_mg,
        "vitamin_d": user_target.vitamin_d_target_mcg,
        "vitamin_b12": user_target.vitamin_b12_target_mcg,
    }

@router.get("/me", response_model=TargetResponse) 
def get_my_target(current_user : User = Depends(get_current_user), db : Session = Depends(get_db)):

    user_target = db.query(UserTarget).filter(UserTarget.user_id == current_user.id).first()

    if user_target is None:
        raise HTTPException(status_code=404, detail="Targets have not been calculated yet")
    
    return build_target_response(user_target=user_target, user=current_user)


@router.post("/calculate", response_model=TargetResponse)
def calculate_my_targets(current_user : User = Depends(get_current_user), db : Session = Depends(get_db)):
    user_target =  calculate_and_save_targets(user=current_user, db=db)
    db.commit()
    db.refresh(user_target)
    return build_target_response(user_target=user_target, user=current_user)

