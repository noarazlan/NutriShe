from decimal import Decimal
from pydantic import BaseModel


class FoodResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    image_url: str | None = None
    calories_per_100g: Decimal
    protein_per_100g: Decimal
    carbohydrates_per_100g: Decimal
    fat_per_100g: Decimal
    fiber_per_100g: Decimal | None = None

    class Config:
        from_attributes = True
        