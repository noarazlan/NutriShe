from sqlalchemy.orm import Session

from data.models.preference import Preference
from data.models.recipe import Recipe, RecipePreference


RECIPES = [
    {
        "name": "Greek Yogurt Berry Bowl",
        "description": "A quick breakfast containing protein and fruit.",
        "ingredients_text": (
            "200 g plain Greek yogurt\n"
            "100 g mixed berries\n"
            "20 g oats\n"
            "5 g chia seeds"
        ),
        "instructions": (
            "Place the yogurt in a bowl. "
            "Add the berries, oats, and chia seeds."
        ),
        "preparation_time_minutes": 5,
        "servings": 1,
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Chicken Quinoa Bowl",
        "description": "A balanced bowl with chicken, quinoa, and vegetables.",
        "ingredients_text": (
            "150 g cooked chicken breast\n"
            "150 g cooked quinoa\n"
            "Mixed vegetables\n"
            "1 tablespoon olive oil\n"
            "Lemon juice"
        ),
        "instructions": (
            "Place all ingredients in a bowl. "
            "Add olive oil and lemon juice before serving."
        ),
        "preparation_time_minutes": 25,
        "servings": 1,
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Lentil Vegetable Soup",
        "description": "A plant-based soup rich in fiber.",
        "ingredients_text": (
            "250 g cooked lentils\n"
            "1 carrot\n"
            "1 onion\n"
            "2 celery stalks\n"
            "400 ml vegetable stock\n"
            "Spices"
        ),
        "instructions": (
            "Cook the onion and vegetables. "
            "Add lentils and stock. "
            "Simmer for approximately 20 minutes."
        ),
        "preparation_time_minutes": 35,
        "servings": 4,
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
    {
        "name": "Tofu Vegetable Stir Fry",
        "description": "A plant-based meal with tofu and vegetables.",
        "ingredients_text": (
            "200 g firm tofu\n"
            "Bell pepper\n"
            "Broccoli\n"
            "Mushrooms\n"
            "Low-sodium soy sauce\n"
            "1 teaspoon sesame oil"
        ),
        "instructions": (
            "Cook the tofu until lightly browned. "
            "Add the vegetables and sauce. "
            "Cook until the vegetables are tender."
        ),
        "preparation_time_minutes": 20,
        "servings": 2,
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Chickpea Avocado Salad",
        "description": "A simple salad containing fiber and unsaturated fat.",
        "ingredients_text": (
            "200 g cooked chickpeas\n"
            "1 avocado\n"
            "Tomato\n"
            "Cucumber\n"
            "Parsley\n"
            "Lemon juice"
        ),
        "instructions": (
            "Combine all ingredients in a bowl. "
            "Add lemon juice and season before serving."
        ),
        "preparation_time_minutes": 10,
        "servings": 2,
        "preferences": [
            "vegan",
            "vegetarian",
            "gluten_free",
            "lactose_free",
        ],
    },
]


def seed_recipes(db: Session) -> None:
    preferences_by_code = {
        preference.code: preference
        for preference in db.query(Preference).all()
    }

    for item in RECIPES:
        preference_codes = item["preferences"]

        recipe = (
            db.query(Recipe)
            .filter(Recipe.name == item["name"])
            .first()
        )

        recipe_values = {
            key: value
            for key, value in item.items()
            if key != "preferences"
        }

        recipe_values["image_url"] = None
        recipe_values["is_active"] = True

        if recipe is None:
            recipe = Recipe(**recipe_values)
            db.add(recipe)
            db.flush()
        else:
            for key, value in recipe_values.items():
                setattr(recipe, key, value)

        (
            db.query(RecipePreference)
            .filter(RecipePreference.recipe_id == recipe.id)
            .delete()
        )

        for preference_code in preference_codes:
            preference = preferences_by_code.get(preference_code)

            if preference:
                db.add(
                    RecipePreference(
                        recipe_id=recipe.id,
                        preference_id=preference.id,
                    )
                )

    db.commit()