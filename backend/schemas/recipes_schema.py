from pydantic import BaseModel
from data.models.enums import MealType


class PreferenceDetailsResponse(BaseModel):
    code: str
    display_name: str

    class Config:
        from_attributes = True


class RecipePreferenceResponse(BaseModel):
    preference: PreferenceDetailsResponse

    class Config:
        from_attributes = True


class RecipeMealTypeResponse(BaseModel):
    meal_type: MealType

    class Config:
        from_attributes = True


class RecipeCardResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    image_url: str | None = None
    preparation_time_minutes: int | None = None
    servings: int | None = None

    class Config:
        from_attributes = True


class RecipeDetailsResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    image_url: str | None = None
    preparation_time_minutes: int | None = None
    servings: int | None = None
    ingredients_text: str | None = None
    instructions: str | None = None

    meal_types: list[RecipeMealTypeResponse] = []
    preferences: list[RecipePreferenceResponse] = []

    class Config:
        from_attributes = True