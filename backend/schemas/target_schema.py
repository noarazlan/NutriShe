from pydantic import BaseModel


class TargetResponse(BaseModel):
    full_name: str
    calories: float
    protein: float
    fat: float
    carbohydrates: float
    fiber: float | None = None

    iron: float | None = None
    calcium: float | None = None
    magnesium: float | None = None
    potassium: float | None = None
    sodium: float | None = None
    vitamin_a: float | None = None
    vitamin_c: float | None = None
    vitamin_d: float | None = None
    vitamin_b12: float | None = None