from sqlalchemy.orm import Session

from data.models.enums import MealType
from data.models.preference import Preference
from data.models.recipe import Recipe, RecipeMealType, RecipePreference


def recipe(
    name,
    description,
    ingredients,
    instructions,
    preparation_time_minutes,
    servings,
    preferences,
    meal_types,
):
    return {
        "name": name,
        "description": description,
        "ingredients_text": "\n".join(ingredients),
        "instructions": instructions,
        "preparation_time_minutes": preparation_time_minutes,
        "servings": servings,
        "preferences": preferences,
        "meal_types": meal_types,
    }


RECIPES = [
    recipe(
        "Greek Yogurt Berry Bowl",
        "A quick breakfast containing protein and fruit.",
        [
            "200 g plain Greek yogurt",
            "100 g mixed berries",
            "20 g gluten-free oats",
            "5 g chia seeds",
        ],
        "Place the yogurt in a bowl. Add the berries, oats, and chia seeds.",
        5,
        1,
        ["vegetarian", "gluten_free"],
        ["breakfast"],
    ),
    recipe(
        "Chicken Quinoa Bowl",
        "A balanced bowl with chicken, quinoa, and vegetables.",
        [
            "150 g cooked chicken breast",
            "150 g cooked quinoa",
            "Mixed vegetables",
            "1 tablespoon olive oil",
            "Lemon juice",
        ],
        "Place all ingredients in a bowl. Add olive oil and lemon juice before serving.",
        25,
        1,
        ["gluten_free", "lactose_free"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Lentil Vegetable Soup",
        "A plant-based soup rich in fiber.",
        [
            "250 g cooked lentils",
            "1 carrot",
            "1 onion",
            "2 celery stalks",
            "400 ml vegetable stock",
            "Spices",
        ],
        "Cook the onion and vegetables. Add the lentils and stock. Simmer for approximately 20 minutes.",
        35,
        4,
        ["vegan", "vegetarian", "gluten_free", "lactose_free"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Tofu Vegetable Stir Fry",
        "A plant-based meal with tofu and vegetables.",
        [
            "200 g firm tofu",
            "1 bell pepper",
            "1 cup broccoli",
            "1 cup mushrooms",
            "Low-sodium soy sauce",
            "1 teaspoon sesame oil",
        ],
        "Cook the tofu until lightly browned. Add the vegetables and sauce. Cook until the vegetables are tender.",
        20,
        2,
        ["vegan", "vegetarian", "lactose_free"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Chickpea Avocado Salad",
        "A simple salad containing fiber and unsaturated fat.",
        [
            "200 g cooked chickpeas",
            "1 avocado",
            "1 tomato",
            "1 cucumber",
            "Fresh parsley",
            "Lemon juice",
        ],
        "Combine all ingredients in a bowl. Add lemon juice and season before serving.",
        10,
        2,
        ["vegan", "vegetarian", "gluten_free", "lactose_free"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Healthy Crackers",
        "Crispy homemade crackers made with gluten-free oat flour, almond flour, seeds, and olive oil.",
        [
            "1 cup gluten-free oat flour",
            "1/2 cup almond flour",
            "2 tablespoons ground flaxseed",
            "2 tablespoons sesame seeds",
            "2 tablespoons sunflower seeds",
            "1 teaspoon salt",
            "3 tablespoons olive oil",
            "1/2 cup water",
        ],
        "Preheat the oven to 170°C. Mix the dry ingredients. Add the oil and water and form a dough. Roll thinly between parchment sheets, cut into squares, and bake for 20–25 minutes until crisp.",
        35,
        8,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["snack"],
    ),
    recipe(
        "Chocolate Peanut Energy Balls",
        "No-bake chocolate energy balls made with oats, peanut butter, cocoa, and coconut.",
        [
            "1 cup gluten-free rolled oats",
            "1/2 cup natural peanut butter",
            "2 tablespoons unsweetened cocoa powder",
            "2 to 3 tablespoons pure maple syrup or unsweetened date syrup",
            "1 teaspoon vanilla extract",
            "Pinch of salt",
            "Shredded coconut for coating",
        ],
        "Blend the oats briefly. Mix with the remaining ingredients, refrigerate for 20 minutes, roll into balls, and coat with coconut.",
        30,
        12,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["snack"],
    ),
    recipe(
        "Buckwheat Bread",
        "A naturally gluten-free vegan bread made with soaked green buckwheat.",
        [
            "2 cups raw green buckwheat groats",
            "1 1/2 cups water",
            "1 tablespoon chia seeds",
            "1 tablespoon psyllium husk",
            "1 teaspoon salt",
            "1 teaspoon baking powder",
        ],
        "Soak the buckwheat for 8–12 hours, drain, rinse, and blend with fresh water. Add the remaining ingredients, pour into a loaf pan, and bake at 180°C for about 70 minutes.",
        80,
        12,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["breakfast", "snack"],
    ),
    recipe(
        "Healthy Banana Muffins",
        "Soft gluten-free banana muffins made with eggs, almond flour, and oat flour.",
        [
            "3 ripe bananas",
            "2 eggs",
            "1/4 cup melted coconut oil or light olive oil",
            "1 teaspoon vanilla extract",
            "1 1/2 cups almond flour",
            "1/2 cup gluten-free oat flour",
            "1 teaspoon baking powder",
            "1 teaspoon cinnamon",
            "50 g dairy-free dark chocolate, optional",
        ],
        "Preheat the oven to 175°C. Mash the bananas, add the wet ingredients, then the dry ingredients. Divide into a muffin tin and bake for 20–25 minutes.",
        35,
        10,
        ["gluten_free", "lactose_free", "vegetarian"],
        ["breakfast", "snack"],
    ),
    recipe(
        "Healthy Vegan Banana Muffins",
        "Soft vegan and gluten-free banana muffins made with flax eggs.",
        [
            "3 ripe bananas",
            "2 tablespoons ground flaxseed",
            "6 tablespoons water",
            "1/4 cup melted coconut oil or light olive oil",
            "1 teaspoon vanilla extract",
            "1 1/2 cups almond flour",
            "1/2 cup gluten-free oat flour",
            "1 teaspoon baking powder",
            "1 teaspoon cinnamon",
            "50 g dairy-free dark chocolate, optional",
        ],
        "Mix the flaxseed with water and rest for 10 minutes. Preheat the oven to 175°C. Mash the bananas, add the wet ingredients, then the dry ingredients. Bake for 20–25 minutes.",
        45,
        10,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["breakfast", "snack"],
    ),
    recipe(
        "Healthy Chocolate Cake",
        "A gluten-free chocolate cake made with eggs and Greek yogurt.",
        [
            "2 eggs",
            "1/2 cup Greek yogurt",
            "1/4 cup light olive oil",
            "1/4 cup pure maple syrup or honey",
            "1/2 cup unsweetened cocoa powder",
            "1 cup almond flour",
            "1/2 cup gluten-free oat flour",
            "1 teaspoon baking powder",
            "Pinch of salt",
        ],
        "Preheat the oven to 175°C. Mix the wet ingredients, add the dry ingredients, pour into a pan, and bake for 30–35 minutes.",
        45,
        10,
        ["gluten_free", "vegetarian"],
        ["snack"],
    ),
    recipe(
        "Healthy Vegan Chocolate Cake",
        "A vegan and gluten-free chocolate cake made with flax eggs and plant-based yogurt.",
        [
            "2 tablespoons ground flaxseed",
            "6 tablespoons water",
            "1/2 cup unsweetened soy yogurt or coconut yogurt",
            "1/4 cup light olive oil",
            "1/4 cup pure maple syrup",
            "1/2 cup unsweetened cocoa powder",
            "1 cup almond flour",
            "1/2 cup gluten-free oat flour",
            "1 teaspoon baking powder",
            "Pinch of salt",
        ],
        "Mix the flaxseed with water and rest for 10 minutes. Preheat the oven to 175°C. Mix the wet ingredients, add the dry ingredients, and bake for 30–35 minutes.",
        55,
        10,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["snack"],
    ),
    recipe(
        "Healthy Chocolate Chip Cookies",
        "Gluten-free almond flour cookies made with egg and dark chocolate.",
        [
            "2 cups almond flour",
            "1 egg",
            "3 tablespoons coconut oil",
            "3 tablespoons pure maple syrup or honey",
            "1 teaspoon vanilla extract",
            "1/2 teaspoon baking powder",
            "70 g dairy-free dark chocolate, chopped",
        ],
        "Preheat the oven to 175°C. Mix the ingredients, form small balls, flatten them, and bake for 10–12 minutes.",
        22,
        12,
        ["gluten_free", "lactose_free", "vegetarian"],
        ["snack"],
    ),
    recipe(
        "Healthy Vegan Chocolate Chip Cookies",
        "Vegan and gluten-free almond flour cookies made with a flax egg.",
        [
            "2 cups almond flour",
            "1 tablespoon ground flaxseed",
            "3 tablespoons water",
            "3 tablespoons coconut oil",
            "3 tablespoons pure maple syrup",
            "1 teaspoon vanilla extract",
            "1/2 teaspoon baking powder",
            "70 g dairy-free dark chocolate, chopped",
        ],
        "Mix the flaxseed with water and rest for 10 minutes. Preheat the oven to 175°C. Add the remaining ingredients, form balls, flatten, and bake for 10–12 minutes.",
        32,
        12,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["snack"],
    ),
    recipe(
        "Healthy Vegetable Casserole",
        "A savory gluten-free vegetable bake made with eggs.",
        [
            "2 medium zucchinis, grated",
            "2 carrots, grated",
            "1 onion, finely chopped",
            "3 eggs",
            "1/2 cup gluten-free oat flour",
            "1/4 cup almond flour",
            "2 tablespoons olive oil",
            "1 teaspoon baking powder",
            "Salt, pepper, garlic powder, and oregano",
        ],
        "Preheat the oven to 180°C. Squeeze the zucchini, mix all ingredients, pour into a baking dish, and bake for 35–40 minutes.",
        55,
        6,
        ["gluten_free", "lactose_free", "vegetarian"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Healthy Vegan Vegetable Casserole",
        "A savory vegan and gluten-free vegetable bake made with chickpea flour.",
        [
            "2 medium zucchinis, grated",
            "2 carrots, grated",
            "1 onion, finely chopped",
            "3/4 cup chickpea flour",
            "3/4 cup water",
            "1/2 cup gluten-free oat flour",
            "1/4 cup almond flour",
            "2 tablespoons olive oil",
            "1 teaspoon baking powder",
            "Salt, pepper, garlic powder, and oregano",
        ],
        "Preheat the oven to 180°C. Squeeze the zucchini. Mix the chickpea flour with water, combine with the remaining ingredients, and bake for 35–40 minutes.",
        55,
        6,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Tahini Bread",
        "A gluten-free bread made with tahini and eggs.",
        [
            "1 cup tahini",
            "3 eggs",
            "2 tablespoons psyllium husk",
            "1 teaspoon baking powder",
            "1/2 teaspoon salt",
            "1 tablespoon sesame seeds, optional",
        ],
        "Preheat the oven to 180°C. Mix all ingredients, pour into a loaf pan, and bake for 30–35 minutes.",
        45,
        10,
        ["gluten_free", "lactose_free", "vegetarian"],
        ["breakfast", "snack"],
    ),
    recipe(
        "Vegan Tahini Bread",
        "A vegan and gluten-free tahini bread made with flax eggs.",
        [
            "1 cup tahini",
            "3 tablespoons ground flaxseed",
            "9 tablespoons water",
            "2 tablespoons psyllium husk",
            "1 teaspoon baking powder",
            "1/2 teaspoon salt",
            "1 tablespoon sesame seeds, optional",
        ],
        "Mix the flaxseed with water and rest for 10 minutes. Preheat the oven to 180°C. Mix all ingredients, pour into a loaf pan, and bake for 30–35 minutes.",
        55,
        10,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["breakfast", "snack"],
    ),
    recipe(
        "Healthy Banana Pancakes",
        "Gluten-free banana pancakes made with eggs.",
        [
            "2 ripe bananas",
            "2 eggs",
            "1/2 cup gluten-free oat flour",
            "1/2 cup almond flour",
            "1 teaspoon baking powder",
            "1 teaspoon cinnamon",
            "1 teaspoon vanilla extract",
            "2 to 4 tablespoons plant-based milk, if needed",
        ],
        "Mash the bananas, whisk in the eggs and vanilla, add the dry ingredients, and cook each pancake for 2–3 minutes per side.",
        25,
        4,
        ["gluten_free", "lactose_free", "vegetarian"],
        ["breakfast"],
    ),
    recipe(
        "Healthy Vegan Banana Pancakes",
        "Vegan and gluten-free banana pancakes made with flax eggs.",
        [
            "2 ripe bananas",
            "2 tablespoons ground flaxseed",
            "6 tablespoons water",
            "1/2 cup gluten-free oat flour",
            "1/2 cup almond flour",
            "1 teaspoon baking powder",
            "1 teaspoon cinnamon",
            "1 teaspoon vanilla extract",
            "2 to 4 tablespoons plant-based milk, if needed",
        ],
        "Mix the flaxseed with water and rest for 10 minutes. Mash the bananas, add the remaining ingredients, and cook each pancake for 2–3 minutes per side.",
        35,
        4,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["breakfast"],
    ),
    recipe(
        "Peanut Butter Banana Date Bites",
        "Frozen date bites with peanut butter, banana, dark chocolate, peanuts, and sea salt.",
        [
            "For 1 bite:",
            "10 g date",
            "3 g natural peanut butter",
            "10 g banana",
            "3 g dairy-free dark chocolate",
            "A small sprinkle of crushed peanuts",
            "Flaky sea salt",
            "A tiny amount of coconut oil, optional",
        ],
        "Open and flatten the date. Add peanut butter and banana. Drizzle with melted chocolate, top with peanuts and salt, and freeze for at least 30 minutes.",
        35,
        1,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["snack"],
    ),
    recipe(
        "No-Bake Cookie Dough Bars",
        "No-bake vegan cookie dough bars with peanut butter and dark chocolate.",
        [
            "70 g gluten-free oat flour",
            "50 g almond flour",
            "50 g natural peanut butter",
            "40 ml pure maple syrup",
            "30 g dairy-free chocolate chips",
            "1 teaspoon vanilla extract",
            "70 g dairy-free dark chocolate, melted",
        ],
        "Mix all ingredients except the melted chocolate. Press into a lined container, cover with melted chocolate, chill until firm, and cut into 10 bars.",
        20,
        10,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["snack"],
    ),
    recipe(
        "Light Meatballs in Red Tomato Sauce",
        "Lean beef meatballs with grated vegetables in a homemade tomato sauce.",
        [
            "Meatballs:",
            "Ground beef",
            "Medium zucchinis",
            "Medium carrot",
            "Fine instant oats",
            "Medium onion",
            "1 bunch parsley",
            "1 large egg",
            "Garlic powder",
            "Fine salt",
            "Ground black pepper",
            "Sweet paprika",
            "Ground cumin",
            "",
            "Sauce:",
            "Large tomatoes",
            "Tomato paste",
            "Medium leek",
            "Celery stalks",
            "Canola oil",
            "3/4 cup boiling water, vegetable stock, or chicken stock",
        ],
        "Peel and grate the carrot, onion, and zucchinis. Blanch, peel, and dice the tomatoes. Slice the leek and celery. Mix the meatball ingredients and form about 18 balls. Sauté the leek, add celery and tomatoes, and cook for 2 minutes. Add tomato paste and liquid and cook for 5 minutes. Add the meatballs, partially cover, and cook for 30–40 minutes.",
        60,
        6,
        ["lactose_free"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Quinoa with Carrots",
        "A lightly sweet and savory quinoa dish with carrots, onion, date syrup, and cumin.",
        [
            "Quinoa, rinsed and drained",
            "Large carrots, grated",
            "Medium onion, chopped",
            "2 tablespoons olive oil",
            "Boiling water",
            "1 level spoon date syrup",
            "Cumin",
            "Salt",
            "Pinch of black pepper",
        ],
        "Sauté the onion in olive oil until lightly golden. Add the carrots and cook for 5 minutes. Add quinoa and seasonings, pour in boiling water, bring to a boil, cover, and cook for 20 minutes. Turn off the heat and leave covered for 10 minutes.",
        30,
        6,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Paprika Turkey Breast",
        "Tender turkey breast cubes cooked with onions and paprika.",
        [
            "Turkey breast, cut into cubes",
            "Onions, chopped",
            "Oil",
            "Heaped spoonfuls of sweet paprika",
            "Salt",
            "Black pepper",
            "Boiling water",
        ],
        "Cook the onions in oil until translucent. Add the turkey and brown it. Add the spices and mix well. Pour in boiling water, bring to a bubble, reduce the heat, cover, and cook for about 30 minutes.",
        35,
        6,
        ["gluten_free", "lactose_free"],
        ["lunch", "dinner"],
    ),
    recipe(
        "Beans in Tomato Sauce",
        "A simple plant-based bean dish cooked in tomato sauce.",
        [
            "Onion, finely chopped",
            "Garlic cloves, chopped",
            "Tomatoes, finely chopped",
            "Tomato paste",
            "Oil",
            "Salt",
            "Black pepper",
            "Beans",
            "Boiling water",
        ],
        "Cook the onion in oil until translucent. Add the garlic and cook for 1 minute. Add the tomato paste, boiling water, salt, and pepper. Add the beans and cook until heated through and the sauce thickens.",
        40,
        5,
        ["gluten_free", "lactose_free", "vegetarian", "vegan"],
        ["lunch", "dinner"],
    ),
]



IMAGE_URLS = {
    "Greek Yogurt Berry Bowl": "/images/recipes/Greek-Yogurt-with-Granola-and-Fruit-bowl.jpg",
    "Chicken Quinoa Bowl": "/images/recipes/Chicken_Quinoa_Bowl.jpg",
    "Lentil Vegetable Soup": "/images/recipes/Lentil_Vegetable_Soup.jpg",
    "Tofu Vegetable Stir Fry": "/images/recipes/Tofu_Vegetable_Stir_Fry.jpg",
    "Chickpea Avocado Salad": "/images/recipes/Chickpea_Avocado_Salad.jpg",
    "Healthy Crackers": "/images/recipes/Healthy_Crackers.jpg",
    "Chocolate Peanut Energy Balls": "/images/recipes/Chocolate_Peanut_Energy_Balls.jpg",
    "Buckwheat Bread": "/images/recipes/Buckwheat_Bread.jpg",
    "Healthy Banana Muffins": "/images/recipes/Healthy_Banana_Muffins.jpg",
    "Healthy Vegan Banana Muffins": "/images/recipes/Healthy_Banana_Muffins.jpg",
    "Healthy Chocolate Cake": "/images/recipes/Healthy_Chocolate_Cake.jpg",
    "Healthy Vegan Chocolate Cake": "/images/recipes/Healthy_Chocolate_Cake.jpg",
    "Healthy Chocolate Chip Cookies": "/images/recipes/Healthy_Chocolate_Chip_Cookies.jpg",
    "Healthy Vegan Chocolate Chip Cookies": "/images/recipes/Healthy_Chocolate_Chip_Cookies.jpg",
    "Healthy Vegetable Casserole": "/images/recipes/Healthy_Vegetable_Casserole.jpg",
    "Healthy Vegan Vegetable Casserole": "/images/recipes/Healthy_Vegetable_Casserole.jpg",
    "Tahini Bread": "/images/recipes/Tahini_Bread.jpg",
    "Vegan Tahini Bread": "/images/recipes/Tahini_Bread.jpg",
    "Healthy Banana Pancakes": "/images/recipes/Healthy_Banana_Pancakes.jpg",
    "Healthy Vegan Banana Pancakes": "/images/recipes/Healthy_Banana_Pancakes.jpg",
    "Peanut Butter Banana Date Bites": "/images/recipes/Peanut_Butter_Banana_Date_Bites.jpg",
    "No-Bake Cookie Dough Bars": "/images/recipes/No-Bake_Cookie_Dough_Bars.jpg",
    "Light Meatballs in Red Tomato Sauce": "/images/recipes/Light_Meatballs_in_Red_Tomato_Sauce.jpg",
    "Quinoa with Carrots": "/images/recipes/Quinoa_with_Carrots.jpg",
    "Paprika Turkey Breast": "/images/recipes/Paprika_Turkey_Breast.jpg",
    "Beans in Tomato Sauce": "/images/recipes/Beans_in_Tomato_Sauce.jpg",
}

def seed_recipes(db: Session) -> None:
    preferences_by_code = {
        preference.code: preference
        for preference in db.query(Preference).all()
    }

    for item in RECIPES:
        preference_codes = item["preferences"]
        meal_type_values = item["meal_types"]

        recipe_obj = (
            db.query(Recipe)
            .filter(Recipe.name == item["name"])
            .first()
        )

        recipe_values = {
            key: value
            for key, value in item.items()
            if key not in {"preferences", "meal_types"}
        }
        recipe_values["image_url"] = IMAGE_URLS.get(item["name"])
        recipe_values["is_active"] = True

        if recipe_obj is None:
            recipe_obj = Recipe(**recipe_values)
            db.add(recipe_obj)
            db.flush()
        else:
            for key, value in recipe_values.items():
                setattr(recipe_obj, key, value)

        (
            db.query(RecipePreference)
            .filter(RecipePreference.recipe_id == recipe_obj.id)
            .delete(synchronize_session=False)
        )

        for preference_code in preference_codes:
            preference = preferences_by_code.get(preference_code)

            if preference is None:
                print(
                    f"Warning: preference '{preference_code}' "
                    f"was not found for recipe '{recipe_obj.name}'."
                )
                continue

            db.add(
                RecipePreference(
                    recipe_id=recipe_obj.id,
                    preference_id=preference.id,
                )
            )

        (
            db.query(RecipeMealType)
            .filter(RecipeMealType.recipe_id == recipe_obj.id)
            .delete(synchronize_session=False)
        )

        for meal_type_value in meal_type_values:
            db.add(
                RecipeMealType(
                    recipe_id=recipe_obj.id,
                    meal_type=MealType(meal_type_value),
                )
            )

    db.commit()
    print(f"{len(RECIPES)} recipes seeded successfully.")