from sqlalchemy.orm import Session

from data.models.enums import LifeStage, ReferenceType
from data.models.reference import NutrientReferenceValue


SOURCE_NAME = "National Academies Dietary Reference Intakes"
SOURCE_URL = (
    "https://www.nationalacademies.org/"
    "our-work/summary-report-of-the-dietary-reference-intakes"
)


REFERENCE_VALUES = [
    # Women aged 19–30
    ("fiber", "Fiber", "g", 19, 30, 25, None, ReferenceType.AI),
    ("iron", "Iron", "mg", 19, 30, 18, 45, ReferenceType.RDA),
    ("calcium", "Calcium", "mg", 19, 30, 1000, 2500, ReferenceType.RDA),
    ("magnesium", "Magnesium", "mg", 19, 30, 310, 350, ReferenceType.RDA),
    ("potassium", "Potassium", "mg", 19, 30, 2600, None, ReferenceType.AI),
    ("sodium", "Sodium", "mg", 19, 30, 1500, 2300, ReferenceType.AI),
    ("vitamin_a", "Vitamin A", "mcg RAE", 19, 30, 700, 3000, ReferenceType.RDA),
    ("vitamin_c", "Vitamin C", "mg", 19, 30, 75, 2000, ReferenceType.RDA),
    ("vitamin_d", "Vitamin D", "mcg", 19, 30, 15, 100, ReferenceType.RDA),
    ("vitamin_b12", "Vitamin B12", "mcg", 19, 30, 2.4, None, ReferenceType.RDA),
    ("folate", "Folate", "mcg DFE", 19, 30, 400, 1000, ReferenceType.RDA),

    # Women aged 31–50
    ("fiber", "Fiber", "g", 31, 50, 25, None, ReferenceType.AI),
    ("iron", "Iron", "mg", 31, 50, 18, 45, ReferenceType.RDA),
    ("calcium", "Calcium", "mg", 31, 50, 1000, 2500, ReferenceType.RDA),
    ("magnesium", "Magnesium", "mg", 31, 50, 320, 350, ReferenceType.RDA),
    ("potassium", "Potassium", "mg", 31, 50, 2600, None, ReferenceType.AI),
    ("sodium", "Sodium", "mg", 31, 50, 1500, 2300, ReferenceType.AI),
    ("vitamin_a", "Vitamin A", "mcg RAE", 31, 50, 700, 3000, ReferenceType.RDA),
    ("vitamin_c", "Vitamin C", "mg", 31, 50, 75, 2000, ReferenceType.RDA),
    ("vitamin_d", "Vitamin D", "mcg", 31, 50, 15, 100, ReferenceType.RDA),
    ("vitamin_b12", "Vitamin B12", "mcg", 31, 50, 2.4, None, ReferenceType.RDA),
    ("folate", "Folate", "mcg DFE", 31, 50, 400, 1000, ReferenceType.RDA),

    # Women aged 51–70
    ("fiber", "Fiber", "g", 51, 70, 21, None, ReferenceType.AI),
    ("iron", "Iron", "mg", 51, 70, 8, 45, ReferenceType.RDA),
    ("calcium", "Calcium", "mg", 51, 70, 1200, 2000, ReferenceType.RDA),
    ("magnesium", "Magnesium", "mg", 51, 70, 320, 350, ReferenceType.RDA),
    ("potassium", "Potassium", "mg", 51, 70, 2600, None, ReferenceType.AI),
    ("sodium", "Sodium", "mg", 51, 70, 1500, 2300, ReferenceType.AI),
    ("vitamin_a", "Vitamin A", "mcg RAE", 51, 70, 700, 3000, ReferenceType.RDA),
    ("vitamin_c", "Vitamin C", "mg", 51, 70, 75, 2000, ReferenceType.RDA),
    ("vitamin_d", "Vitamin D", "mcg", 51, 70, 15, 100, ReferenceType.RDA),
    ("vitamin_b12", "Vitamin B12", "mcg", 51, 70, 2.4, None, ReferenceType.RDA),
    ("folate", "Folate", "mcg DFE", 51, 70, 400, 1000, ReferenceType.RDA),

    # Women aged 71+
    ("fiber", "Fiber", "g", 71, 120, 21, None, ReferenceType.AI),
    ("iron", "Iron", "mg", 71, 120, 8, 45, ReferenceType.RDA),
    ("calcium", "Calcium", "mg", 71, 120, 1200, 2000, ReferenceType.RDA),
    ("magnesium", "Magnesium", "mg", 71, 120, 320, 350, ReferenceType.RDA),
    ("potassium", "Potassium", "mg", 71, 120, 2600, None, ReferenceType.AI),
    ("sodium", "Sodium", "mg", 71, 120, 1500, 2300, ReferenceType.AI),
    ("vitamin_a", "Vitamin A", "mcg RAE", 71, 120, 700, 3000, ReferenceType.RDA),
    ("vitamin_c", "Vitamin C", "mg", 71, 120, 75, 2000, ReferenceType.RDA),
    ("vitamin_d", "Vitamin D", "mcg", 71, 120, 20, 100, ReferenceType.RDA),
    ("vitamin_b12", "Vitamin B12", "mcg", 71, 120, 2.4, None, ReferenceType.RDA),
    ("folate", "Folate", "mcg DFE", 71, 120, 400, 1000, ReferenceType.RDA),
]


def seed_reference_values(db: Session) -> None:
    for (
        nutrient_code,
        display_name,
        unit,
        min_age,
        max_age,
        recommended_amount,
        upper_limit,
        reference_type,
    ) in REFERENCE_VALUES:

        value = (
            db.query(NutrientReferenceValue)
            .filter(
                NutrientReferenceValue.nutrient_code == nutrient_code,
                NutrientReferenceValue.min_age == min_age,
                NutrientReferenceValue.max_age == max_age,
                NutrientReferenceValue.life_stage == LifeStage.STANDARD,
            )
            .first()
        )

        data = {
            "display_name": display_name,
            "unit": unit,
            "recommended_amount": recommended_amount,
            "upper_limit_amount": upper_limit,
            "reference_type": reference_type,
            "source_name": SOURCE_NAME,
            "source_year": None,
            "source_url": SOURCE_URL,
        }

        if value is None:
            db.add(
                NutrientReferenceValue(
                    nutrient_code=nutrient_code,
                    min_age=min_age,
                    max_age=max_age,
                    life_stage=LifeStage.STANDARD,
                    **data,
                )
            )
        else:
            for key, item_value in data.items():
                setattr(value, key, item_value)

    db.commit()