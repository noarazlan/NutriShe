from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from data.database import get_db
from data.models.user import User
from data.models.tip import Tip, TipPreference
from utils.security import get_current_user
from schemas.tip_schema import TipResponse
import random


router = APIRouter(prefix="/tips",tags=["tips"])

def find_matching_tips(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
     user_preference_codes = {user_preference.preference.code
                                for user_preference in current_user.preferences }
    
     all_tips = (db.query(Tip).options(joinedload(Tip.preferences).joinedload(TipPreference.preference))
            .filter(Tip.is_active.is_(True)).all())
    
     matching_tips = []
    
     for tip in all_tips:
        tip_preference_codes = {tip_preference.preference.code
                                for tip_preference in tip.preferences }
    
        is_general_tip = len(tip_preference_codes) == 0
    
        matches_user_preference = bool(user_preference_codes.intersection(tip_preference_codes ))
    
        if is_general_tip or matches_user_preference:
            matching_tips.append(tip)
    
     return matching_tips

 

@router.get("/all-tips", response_model=list[TipResponse])
def get_all_tips(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    tips = (db.query(Tip).options(joinedload(Tip.preferences).joinedload(TipPreference.preference))
        .filter(Tip.is_active.is_(True)).all())
    return tips


@router.get("/", response_model=list[TipResponse])
def get_tips(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return find_matching_tips(db=db, current_user=current_user)


@router.get("/home", response_model=list[TipResponse])
def get_random_tips(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    matching_tips = find_matching_tips(db=db, current_user=current_user)
    number_of_tips = min(4, len(matching_tips))
    random_tips = random.sample(matching_tips, number_of_tips)
    return random_tips


@router.get("/{tip_id}", response_model=TipResponse)
def get_tip_by_id(tip_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    tip = (db.query(Tip).options( joinedload(Tip.preferences).joinedload(TipPreference.preference))
        .filter(Tip.id == tip_id,Tip.is_active.is_(True)).first())

    if tip is None:
        raise HTTPException(
            status_code=404,
            detail="Tip not found"
        )

    return tip