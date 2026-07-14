from sqlalchemy.orm import Session

from data.models.enums import FoodCategoryType
from data.models.food import Food, FoodCategory, FoodPreference
from data.models.preference import Preference


FOODS = [
    {
        "name": "Chicken Breast, Cooked",
        "calories": 165,
        "protein": 31.0,
        "carbohydrates": 0.0,
        "fat": 3.6,
        "fiber": 0.0,
        "sugar": 0.0,
        "saturated_fat": 1.0,
        "iron": 1.0,
        "calcium": 15,
        "magnesium": 29,
        "potassium": 256,
        "sodium": 74,
        "vitamin_a": 6,
        "vitamin_c": 0,
        "vitamin_d": 0.1,
        "vitamin_b12": 0.3,
        "folate": 4,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Salmon, Cooked",
        "calories": 206,
        "protein": 22.0,
        "carbohydrates": 0.0,
        "fat": 12.0,
        "fiber": 0.0,
        "sugar": 0.0,
        "saturated_fat": 3.1,
        "iron": 0.3,
        "calcium": 12,
        "magnesium": 30,
        "potassium": 384,
        "sodium": 59,
        "vitamin_a": 40,
        "vitamin_c": 0,
        "vitamin_d": 13.0,
        "vitamin_b12": 3.2,
        "folate": 25,
        "categories": ["protein", "fat"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Egg, Whole, Cooked",
        "calories": 155,
        "protein": 12.6,
        "carbohydrates": 1.1,
        "fat": 10.6,
        "fiber": 0.0,
        "sugar": 1.1,
        "saturated_fat": 3.3,
        "iron": 1.2,
        "calcium": 50,
        "magnesium": 10,
        "potassium": 126,
        "sodium": 124,
        "vitamin_a": 149,
        "vitamin_c": 0,
        "vitamin_d": 2.2,
        "vitamin_b12": 1.1,
        "folate": 44,
        "categories": ["protein", "fat"],
        "preferences": ["vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Greek Yogurt, Plain, 2%",
        "calories": 73,
        "protein": 9.9,
        "carbohydrates": 3.9,
        "fat": 1.9,
        "fiber": 0.0,
        "sugar": 3.6,
        "saturated_fat": 1.2,
        "iron": 0.1,
        "calcium": 115,
        "magnesium": 11,
        "potassium": 141,
        "sodium": 34,
        "vitamin_a": 27,
        "vitamin_c": 0,
        "vitamin_d": 0,
        "vitamin_b12": 0.5,
        "folate": 7,
        "categories": ["protein"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Tofu, Firm",
        "calories": 144,
        "protein": 17.3,
        "carbohydrates": 2.8,
        "fat": 8.7,
        "fiber": 2.3,
        "sugar": 0.6,
        "saturated_fat": 1.3,
        "iron": 2.7,
        "calcium": 683,
        "magnesium": 58,
        "potassium": 237,
        "sodium": 14,
        "vitamin_a": 0,
        "vitamin_c": 0.2,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 29,
        "categories": ["protein", "fat"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Lentils, Cooked",
        "calories": 116,
        "protein": 9.0,
        "carbohydrates": 20.1,
        "fat": 0.4,
        "fiber": 7.9,
        "sugar": 1.8,
        "saturated_fat": 0.1,
        "iron": 3.3,
        "calcium": 19,
        "magnesium": 36,
        "potassium": 369,
        "sodium": 2,
        "vitamin_a": 8,
        "vitamin_c": 1.5,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 181,
        "categories": ["protein", "carbohydrates", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Chickpeas, Cooked",
        "calories": 164,
        "protein": 8.9,
        "carbohydrates": 27.4,
        "fat": 2.6,
        "fiber": 7.6,
        "sugar": 4.8,
        "saturated_fat": 0.3,
        "iron": 2.9,
        "calcium": 49,
        "magnesium": 48,
        "potassium": 291,
        "sodium": 7,
        "vitamin_a": 1,
        "vitamin_c": 1.3,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 172,
        "categories": ["protein", "carbohydrates", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Oats, Dry",
        "calories": 379,
        "protein": 13.2,
        "carbohydrates": 67.7,
        "fat": 6.5,
        "fiber": 10.1,
        "sugar": 1.0,
        "saturated_fat": 1.2,
        "iron": 4.3,
        "calcium": 52,
        "magnesium": 138,
        "potassium": 362,
        "sodium": 6,
        "vitamin_a": 0,
        "vitamin_c": 0,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 56,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Brown Rice, Cooked",
        "calories": 123,
        "protein": 2.7,
        "carbohydrates": 25.6,
        "fat": 1.0,
        "fiber": 1.6,
        "sugar": 0.2,
        "saturated_fat": 0.3,
        "iron": 0.6,
        "calcium": 3,
        "magnesium": 39,
        "potassium": 86,
        "sodium": 4,
        "vitamin_a": 0,
        "vitamin_c": 0,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 9,
        "categories": ["carbohydrates", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Quinoa, Cooked",
        "calories": 120,
        "protein": 4.4,
        "carbohydrates": 21.3,
        "fat": 1.9,
        "fiber": 2.8,
        "sugar": 0.9,
        "saturated_fat": 0.2,
        "iron": 1.5,
        "calcium": 17,
        "magnesium": 64,
        "potassium": 172,
        "sodium": 7,
        "vitamin_a": 1,
        "vitamin_c": 0,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 42,
        "categories": ["protein", "carbohydrates", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Sweet Potato, Baked",
        "calories": 90,
        "protein": 2.0,
        "carbohydrates": 20.7,
        "fat": 0.2,
        "fiber": 3.3,
        "sugar": 6.5,
        "saturated_fat": 0,
        "iron": 0.7,
        "calcium": 38,
        "magnesium": 27,
        "potassium": 475,
        "sodium": 36,
        "vitamin_a": 961,
        "vitamin_c": 19.6,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 6,
        "categories": ["carbohydrates", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Olive Oil",
        "calories": 884,
        "protein": 0,
        "carbohydrates": 0,
        "fat": 100,
        "fiber": 0,
        "sugar": 0,
        "saturated_fat": 13.8,
        "iron": 0.6,
        "calcium": 1,
        "magnesium": 0,
        "potassium": 1,
        "sodium": 2,
        "vitamin_a": 0,
        "vitamin_c": 0,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 0,
        "categories": ["fat"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Avocado",
        "calories": 160,
        "protein": 2.0,
        "carbohydrates": 8.5,
        "fat": 14.7,
        "fiber": 6.7,
        "sugar": 0.7,
        "saturated_fat": 2.1,
        "iron": 0.6,
        "calcium": 12,
        "magnesium": 29,
        "potassium": 485,
        "sodium": 7,
        "vitamin_a": 7,
        "vitamin_c": 10,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 81,
        "categories": ["fat", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Almonds",
        "calories": 579,
        "protein": 21.2,
        "carbohydrates": 21.6,
        "fat": 49.9,
        "fiber": 12.5,
        "sugar": 4.4,
        "saturated_fat": 3.8,
        "iron": 3.7,
        "calcium": 269,
        "magnesium": 270,
        "potassium": 733,
        "sodium": 1,
        "vitamin_a": 0,
        "vitamin_c": 0,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 44,
        "categories": ["protein", "fat", "fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Broccoli, Cooked",
        "calories": 35,
        "protein": 2.4,
        "carbohydrates": 7.2,
        "fat": 0.4,
        "fiber": 3.3,
        "sugar": 1.4,
        "saturated_fat": 0.1,
        "iron": 0.7,
        "calcium": 40,
        "magnesium": 21,
        "potassium": 293,
        "sodium": 41,
        "vitamin_a": 77,
        "vitamin_c": 64.9,
        "vitamin_d": 0,
        "vitamin_b12": 0,
        "folate": 108,
        "categories": ["fiber"],
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
]


CATEGORY_MAP = {
    "protein": FoodCategoryType.PROTEIN,
    "carbohydrates": FoodCategoryType.CARBOHYDRATES,
    "fat": FoodCategoryType.FAT,
    "fiber": FoodCategoryType.FIBER,
}


def seed_foods(db: Session) -> None:
    preferences_by_code = {
        preference.code: preference
        for preference in db.query(Preference).all()
    }

    for item in FOODS:
        categories = item["categories"]
        preference_codes = item["preferences"]

        food = (
            db.query(Food)
            .filter(Food.name == item["name"])
            .first()
        )

        food_values = {
            "description": (
                f"Nutrition values for {item['name']} per 100 grams."
            ),
            "image_url": None,
            "calories_per_100g": item["calories"],
            "protein_per_100g": item["protein"],
            "carbohydrates_per_100g": item["carbohydrates"],
            "fat_per_100g": item["fat"],
            "fiber_per_100g": item["fiber"],
            "sugar_per_100g": item["sugar"],
            "saturated_fat_per_100g": item["saturated_fat"],
            "iron_mg_per_100g": item["iron"],
            "calcium_mg_per_100g": item["calcium"],
            "magnesium_mg_per_100g": item["magnesium"],
            "potassium_mg_per_100g": item["potassium"],
            "sodium_mg_per_100g": item["sodium"],
            "vitamin_a_mcg_per_100g": item["vitamin_a"],
            "vitamin_c_mg_per_100g": item["vitamin_c"],
            "vitamin_d_mcg_per_100g": item["vitamin_d"],
            "vitamin_b12_mcg_per_100g": item["vitamin_b12"],
            "folate_mcg_per_100g": item["folate"],
            "data_source": "USDA FoodData Central starter values",
            "is_active": True,
        }

        if food is None:
            food = Food(name=item["name"], **food_values)
            db.add(food)
            db.flush()
        else:
            for key, value in food_values.items():
                setattr(food, key, value)

        (
            db.query(FoodCategory)
            .filter(FoodCategory.food_id == food.id)
            .delete()
        )

        for category_code in categories:
            db.add(
                FoodCategory(
                    food_id=food.id,
                    category=CATEGORY_MAP[category_code],
                )
            )

        (
            db.query(FoodPreference)
            .filter(FoodPreference.food_id == food.id)
            .delete()
        )

        for preference_code in preference_codes:
            preference = preferences_by_code.get(preference_code)

            if preference:
                db.add(
                    FoodPreference(
                        food_id=food.id,
                        preference_id=preference.id,
                    )
                )

    db.commit()