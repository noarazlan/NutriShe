from sqlalchemy.orm import Session

from data.models.enums import TipType
from data.models.preference import Preference
from data.models.tip import Tip, TipPreference


TIPS = [
    # =========================
    # General tips
    # =========================
    {
        "title": "Choose minimally processed foods",
        "content": (
            "Choose foods that are as natural and minimally processed "
            "as possible."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Prefer simple ingredient lists",
        "content": (
            "Prefer products with a short and simple ingredient list."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Limit unnecessary additives",
        "content": (
            "Choose products with as few preservatives, artificial colors, "
            "and unnecessary additives as possible."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Read the ingredient list",
        "content": (
            "Always read the ingredient list, not only the nutrition facts label."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Reduce added sugar",
        "content": (
            "Choose products with little or no added sugar whenever possible."
        ),
        "tip_type": TipType.CARBOHYDRATES,
        "preferences": [],
    },
    {
        "title": "Choose high-fiber foods",
        "content": (
            "Prefer foods that are naturally high in fiber."
        ),
        "tip_type": TipType.FIBER,
        "preferences": [],
    },
    {
        "title": "Include protein regularly",
        "content": (
            "Include a source of protein in each main meal."
        ),
        "tip_type": TipType.PROTEIN,
        "preferences": [],
    },
    {
        "title": "Start meals with vegetables",
        "content": (
            "Starting a meal with vegetables can help you include more fiber "
            "and create a balanced plate."
        ),
        "tip_type": TipType.FIBER,
        "preferences": [],
    },
    {
        "title": "Eat foods in a balanced order",
        "content": (
            "Try eating vegetables first, followed by protein and healthy fats, "
            "and then carbohydrates."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Build balanced meals",
        "content": (
            "Include protein, healthy fats, fiber-rich foods, and a suitable "
            "carbohydrate source in your meals."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Choose fiber-rich carbohydrates",
        "content": (
            "Prefer oats, legumes, quinoa, buckwheat, potatoes, sweet potatoes, "
            "and whole grains over highly refined carbohydrate options."
        ),
        "tip_type": TipType.CARBOHYDRATES,
        "preferences": [],
    },
    {
        "title": "Prefer whole fruit",
        "content": (
            "Prefer whole fruits over fruit juice because whole fruit provides "
            "more fiber and is usually more filling."
        ),
        "tip_type": TipType.CARBOHYDRATES,
        "preferences": [],
    },
    {
        "title": "Eat sweets after a meal",
        "content": (
            "When you want something sweet, having it after a balanced meal "
            "may be more satisfying than eating it on an empty stomach."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Pair sweet snacks",
        "content": (
            "When eating something sweet between meals, consider pairing it "
            "with protein, fiber, or healthy fats."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Eat slowly",
        "content": (
            "Eat slowly and chew your food thoroughly."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Notice hunger and fullness",
        "content": (
            "Pay attention to your hunger and fullness cues while eating."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Drink enough water",
        "content": (
            "Drink water regularly throughout the day."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Prefer unsweetened beverages",
        "content": (
            "Choose water or unsweetened beverages more often than sugary drinks."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Walk after meals",
        "content": (
            "A light 10 to 20 minute walk after a meal can support general "
            "well-being and daily physical activity."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Prioritize quality sleep",
        "content": (
            "Aim for enough consistent, high-quality sleep."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Support stress management",
        "content": (
            "Include stress-reducing habits such as walking, breathing exercises, "
            "rest, or enjoyable activities."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Consider food quality",
        "content": (
            "Do not focus only on calories; also consider ingredient quality, "
            "fiber, protein, vitamins, and minerals."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Prefer regular balanced meals",
        "content": (
            "Regular balanced meals may be more helpful than frequent unplanned "
            "snacking."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Plan meals in advance",
        "content": (
            "Planning meals in advance can make balanced food choices easier."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Eat mindfully",
        "content": (
            "Try to eat without unnecessary distractions and pay attention to "
            "taste, texture, and fullness."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Aim for balance",
        "content": (
            "There is no need to completely avoid favorite foods. Include them "
            "in moderation as part of an overall balanced eating pattern."
        ),
        "tip_type": TipType.GENERAL,
        "preferences": [],
    },
    {
        "title": "Increase fiber gradually",
        "content": (
            "Increase fiber intake gradually and drink enough fluids to reduce "
            "digestive discomfort."
        ),
        "tip_type": TipType.FIBER,
        "preferences": [],
    },
    {
        "title": "Choose unsaturated fats",
        "content": (
            "Use olive oil, avocado, tahini, nuts, and seeds as common sources "
            "of unsaturated fat."
        ),
        "tip_type": TipType.FAT,
        "preferences": [],
    },

    # =========================
    # Gluten-free tips
    # =========================
    {
        "title": "Choose naturally gluten-free foods",
        "content": (
            "Build meals around naturally gluten-free foods such as rice, quinoa, "
            "buckwheat, potatoes, legumes, fruits, vegetables, eggs, fish, and meat."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["gluten_free"],
    },
    {
        "title": "Check gluten-free labels",
        "content": (
            "Check product labels carefully and choose certified gluten-free "
            "products when cross-contamination is a concern."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["gluten_free"],
    },
    {
        "title": "Choose fiber-rich gluten-free grains",
        "content": (
            "Include quinoa, buckwheat, brown rice, and certified gluten-free oats "
            "to improve fiber variety."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["gluten_free"],
    },
    {
        "title": "Limit refined gluten-free snacks",
        "content": (
            "Gluten-free does not always mean nutritious. Compare fiber, added "
            "sugar, and ingredient quality when choosing packaged foods."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["gluten_free"],
    },
    {
        "title": "Prevent gluten cross-contamination",
        "content": (
            "Use clean utensils, preparation surfaces, and storage containers "
            "when avoiding gluten cross-contamination."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["gluten_free"],
    },

    # =========================
    # Lactose-free tips
    # =========================
    {
        "title": "Choose lactose-free alternatives",
        "content": (
            "Choose lactose-free dairy products or suitable plant-based "
            "alternatives according to your tolerance."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["lactose_free"],
    },
    {
        "title": "Look for fortified plant drinks",
        "content": (
            "When choosing plant-based milk or yogurt, prefer products fortified "
            "with calcium and vitamin D."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["lactose_free", "vegan"],
    },
    {
        "title": "Include non-dairy calcium sources",
        "content": (
            "Include calcium-containing foods such as tahini, tofu, almonds, "
            "leafy greens, and fortified products."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["lactose_free", "vegan"],
    },
    {
        "title": "Check hidden lactose sources",
        "content": (
            "Read labels on sauces, baked goods, protein products, and processed "
            "foods because they may contain milk ingredients."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["lactose_free"],
    },
    {
        "title": "Choose alternatives with protein",
        "content": (
            "Some plant-based dairy alternatives are low in protein. Compare "
            "labels and choose higher-protein options when possible."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["lactose_free", "vegan"],
    },

    # =========================
    # Vegetarian tips
    # =========================
    {
        "title": "Include vegetarian protein",
        "content": (
            "Include eggs, dairy products, legumes, tofu, tempeh, nuts, or seeds "
            "throughout the day."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegetarian"],
    },
    {
        "title": "Pair plant iron with vitamin C",
        "content": (
            "Combine lentils, beans, tofu, spinach, or seeds with vitamin C-rich "
            "foods such as peppers, tomatoes, citrus fruit, or strawberries."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegetarian", "vegan"],
    },
    {
        "title": "Pay attention to vitamin B12",
        "content": (
            "Include reliable vitamin B12 sources and discuss supplementation "
            "with a qualified healthcare professional when needed."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegetarian", "vegan"],
    },
    {
        "title": "Vary vegetarian protein sources",
        "content": (
            "Rotate between legumes, soy foods, eggs, dairy products, nuts, and "
            "seeds to improve nutrient variety."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegetarian"],
    },
    {
        "title": "Choose filling vegetarian meals",
        "content": (
            "Build vegetarian meals with protein, vegetables, a fiber-rich "
            "carbohydrate, and healthy fats."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegetarian"],
    },

    # =========================
    # Vegan tips
    # =========================
    {
        "title": "Use varied vegan proteins",
        "content": (
            "Include legumes, tofu, tempeh, edamame, nuts, and seeds throughout "
            "the week."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegan"],
    },
    {
        "title": "Include plant omega-3 sources",
        "content": (
            "Include chia seeds, ground flaxseed, hemp seeds, or walnuts regularly."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegan"],
    },
    {
        "title": "Choose fortified vegan foods",
        "content": (
            "Fortified plant drinks, yogurts, and cereals can help provide "
            "nutrients such as calcium, vitamin D, and vitamin B12."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegan"],
    },
    {
        "title": "Include iodine sources carefully",
        "content": (
            "Pay attention to iodine intake and use appropriate fortified foods "
            "or iodized salt in suitable amounts."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegan"],
    },
    {
        "title": "Build complete vegan meals",
        "content": (
            "Combine a plant protein, vegetables, a fiber-rich carbohydrate, and "
            "healthy fats to create satisfying vegan meals."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["vegan"],
    },

    # =========================
    # PCOS tips
    # =========================
    {
        "title": "Prioritize protein at breakfast",
        "content": (
            "Include a meaningful protein source at breakfast, such as eggs, "
            "Greek yogurt, tofu, or another suitable protein option."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
    {
        "title": "Choose high-fiber carbohydrates for PCOS",
        "content": (
            "Prefer legumes, oats, quinoa, buckwheat, vegetables, and whole fruit "
            "more often than highly refined carbohydrate sources."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
    {
        "title": "Pair carbohydrates with protein",
        "content": (
            "Combine carbohydrate foods with protein, fiber, or healthy fats to "
            "create more balanced meals and snacks."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
    {
        "title": "Reduce sugary drinks for PCOS",
        "content": (
            "Choose water or unsweetened beverages more often than sugary drinks."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
    {
        "title": "Stay physically active with PCOS",
        "content": (
            "Regular walking, resistance training, and other enjoyable physical "
            "activity can support general health."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
    {
        "title": "Maintain a consistent sleep routine",
        "content": (
            "A regular sleep schedule can support energy, appetite regulation, "
            "and overall well-being."
        ),
        "tip_type": TipType.PERSONALIZED,
        "preferences": ["pcos"],
    },
    {
        "title": "Focus on consistent habits",
        "content": (
            "Small habits practiced consistently are usually more sustainable "
            "than strict or highly restrictive diets."
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
            tip = Tip(
                title=item["title"],
                **tip_values,
            )
            db.add(tip)
            db.flush()
        else:
            for key, value in tip_values.items():
                setattr(tip, key, value)

        (
            db.query(TipPreference)
            .filter(TipPreference.tip_id == tip.id)
            .delete(synchronize_session=False)
        )

        for preference_code in preference_codes:
            preference = preferences_by_code.get(preference_code)

            if preference is None:
                print(
                    f"Warning: preference '{preference_code}' "
                    f"was not found for tip '{tip.title}'."
                )
                continue

            db.add(
                TipPreference(
                    tip_id=tip.id,
                    preference_id=preference.id,
                )
            )

    db.commit()
    print(f"{len(TIPS)} tips seeded successfully.")