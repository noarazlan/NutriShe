from sqlalchemy.orm import Session

from data.models.enums import TipType
from data.models.preference import Preference
from data.models.tip import Tip, TipPreference


TIPS = [
    {
        "title": "Build balanced meals",
        "content": (
            "A balanced meal can include a protein source, "
            "a carbohydrate source, vegetables or fruit, "
            "and a source of unsaturated fat."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Increase fiber gradually",
        "content": (
            "Increase fiber intake gradually and drink enough fluids "
            "to reduce digestive discomfort."
        ),
        "tip_type": TipType.FIBER,
        "preferences": [],
    },
    {
        "title": "Include protein regularly",
        "content": (
            "Distribute protein-containing foods across meals "
            "instead of relying on one large serving."
        ),
        "tip_type": TipType.PROTEIN,
        "preferences": [],
    },
    {
        "title": "Prefer minimally processed carbohydrates",
        "content": (
            "Choose oats, potatoes, legumes, quinoa, and whole grains "
            "more often than highly refined carbohydrate options."
        ),
        "tip_type": TipType.CARBOHYDRATES,
        "preferences": [],
    },
    {
        "title": "Choose unsaturated fats",
        "content": (
            "Use foods such as olive oil, avocado, tahini, nuts, "
            "and seeds as common sources of unsaturated fat."
        ),
        "tip_type": TipType.FAT,
        "preferences": [],
    },
    {
        "title": "Vegan protein variety",
        "content": (
            "Include a variety of legumes, tofu, tempeh, grains, "
            "nuts, and seeds throughout the week."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegan"],
    },
    {
        "title": "Vegetarian iron awareness",
        "content": (
            "Include iron-containing plant foods and combine them "
            "with vitamin C-rich foods to support iron absorption."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegetarian", "vegan"],
    },
    {
        "title": "Lactose-free calcium sources",
        "content": (
            "Choose lactose-free dairy products or fortified plant "
            "drinks when calcium intake is a concern."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["lactose_free"],
    },
    {
        "title": "Gluten-free whole foods",
        "content": (
            "Naturally gluten-free foods include rice, quinoa, "
            "potatoes, legumes, fruits, vegetables, eggs, fish, "
            "and unprocessed meat."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["gluten_free"],
    },
    {
        "title": "PCOS and meal balance",
        "content": (
            "Meals containing protein, fiber-rich carbohydrates, "
            "vegetables, and unsaturated fats may support fullness "
            "and steady energy."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
]


def seed_tips(db: Session) -> None:
    preferences_by_code = {
        preference.code: preference
        for preference in db.query(Preference).all()
    }

    for item in TIPS:
        preference_codes = item["preferences"]

        tip = (
            db.query(Tip)
            .filter(Tip.title == item["title"])
            .first()
        )

        tip_values = {
            "content": item["content"],
            "tip_type": item["tip_type"],
            "image_url": None,
            "is_active": True,
        }

        if tip is None:
            tip = Tip(title=item["title"], **tip_values)
            db.add(tip)
            db.flush()
        else:
            for key, value in tip_values.items():
                setattr(tip, key, value)

        (
            db.query(TipPreference)
            .filter(TipPreference.tip_id == tip.id)
            .delete()
        )

        for preference_code in preference_codes:
            preference = preferences_by_code.get(preference_code)

            if preference:
                db.add(
                    TipPreference(
                        tip_id=tip.id,
                        preference_id=preference.id,
                    )
                )

    db.commit()