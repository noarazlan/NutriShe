from sqlalchemy.orm import Session

from data.models.enums import PreferenceType
from data.models.preference import Preference


PREFERENCES = [
    {
        "code": "vegetarian",
        "display_name": "Vegetarian",
        "preference_type": PreferenceType.DIET,
        "description": "A diet that excludes meat and fish.",
    },
    {
        "code": "vegan",
        "display_name": "Vegan",
        "preference_type": PreferenceType.DIET,
        "description": "A diet that excludes all animal-derived products.",
    },
    {
        "code": "gluten_free",
        "display_name": "Gluten Free",
        "preference_type": PreferenceType.RESTRICTION,
        "description": "Excludes foods containing gluten.",
    },
    {
        "code": "lactose_free",
        "display_name": "Lactose Free",
        "preference_type": PreferenceType.RESTRICTION,
        "description": "Excludes foods containing lactose.",
    },
  
    {
        "code": "pcos",
        "display_name": "PCOS",
        "preference_type": PreferenceType.HEALTH_TOPIC,
        "description": "Educational nutrition content related to PCOS.",
    },
]


def seed_preferences(db: Session) -> None:
    for item in PREFERENCES:
        preference = (
            db.query(Preference)
            .filter(Preference.code == item["code"])
            .first()
        )

        if preference is None:
            db.add(Preference(**item))
        else:
            preference.display_name = item["display_name"]
            preference.preference_type = item["preference_type"]
            preference.description = item["description"]

    db.commit()