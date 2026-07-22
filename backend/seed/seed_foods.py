from sqlalchemy.orm import Session

from data.models.enums import FoodCategoryType
from data.models.food import Food, FoodCategory, FoodPreference
from data.models.preference import Preference


FOODS = [
    # ----------------------------------------------------
    # EXISTING STARTER FOODS
    # ----------------------------------------------------
    {
        "name": "Chicken Breast, Cooked",
        "calories": 165, "protein": 31.0, "carbohydrates": 0.0, "fat": 3.6, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 1.0, "iron": 1.0, "calcium": 15, "magnesium": 29,
        "potassium": 256, "sodium": 74, "vitamin_a": 6, "vitamin_c": 0, "vitamin_d": 0.1,
        "vitamin_b12": 0.3, "folate": 4,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Salmon, Cooked",
        "calories": 206, "protein": 22.0, "carbohydrates": 0.0, "fat": 12.0, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 3.1, "iron": 0.3, "calcium": 12, "magnesium": 30,
        "potassium": 384, "sodium": 59, "vitamin_a": 40, "vitamin_c": 0, "vitamin_d": 13.0,
        "vitamin_b12": 3.2, "folate": 25,
        "categories": ["protein", "fat"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Egg, Whole, Cooked",
        "calories": 155, "protein": 12.6, "carbohydrates": 1.1, "fat": 10.6, "fiber": 0.0,
        "sugar": 1.1, "saturated_fat": 3.3, "iron": 1.2, "calcium": 50, "magnesium": 10,
        "potassium": 126, "sodium": 124, "vitamin_a": 149, "vitamin_c": 0, "vitamin_d": 2.2,
        "vitamin_b12": 1.1, "folate": 44,
        "categories": ["protein", "fat"],
        "preferences": ["vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Greek Yogurt, Plain, 2%",
        "calories": 73, "protein": 9.9, "carbohydrates": 3.9, "fat": 1.9, "fiber": 0.0,
        "sugar": 3.6, "saturated_fat": 1.2, "iron": 0.1, "calcium": 115, "magnesium": 11,
        "potassium": 141, "sodium": 34, "vitamin_a": 27, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0.5, "folate": 7,
        "categories": ["protein"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Tofu, Firm",
        "calories": 144, "protein": 17.3, "carbohydrates": 2.8, "fat": 8.7, "fiber": 2.3,
        "sugar": 0.6, "saturated_fat": 1.3, "iron": 2.7, "calcium": 683, "magnesium": 58,
        "potassium": 237, "sodium": 14, "vitamin_a": 0, "vitamin_c": 0.2, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 29,
        "categories": ["protein", "fat"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Lentils, Cooked",
        "calories": 116, "protein": 9.0, "carbohydrates": 20.1, "fat": 0.4, "fiber": 7.9,
        "sugar": 1.8, "saturated_fat": 0.1, "iron": 3.3, "calcium": 19, "magnesium": 36,
        "potassium": 369, "sodium": 2, "vitamin_a": 8, "vitamin_c": 1.5, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 181,
        "categories": ["protein", "carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Chickpeas, Cooked",
        "calories": 164, "protein": 8.9, "carbohydrates": 27.4, "fat": 2.6, "fiber": 7.6,
        "sugar": 4.8, "saturated_fat": 0.3, "iron": 2.9, "calcium": 49, "magnesium": 48,
        "potassium": 291, "sodium": 7, "vitamin_a": 1, "vitamin_c": 1.3, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 172,
        "categories": ["protein", "carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Oats, Dry",
        "calories": 379, "protein": 13.2, "carbohydrates": 67.7, "fat": 6.5, "fiber": 10.1,
        "sugar": 1.0, "saturated_fat": 1.2, "iron": 4.3, "calcium": 52, "magnesium": 138,
        "potassium": 362, "sodium": 6, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 56,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Brown Rice, Cooked",
        "calories": 123, "protein": 2.7, "carbohydrates": 25.6, "fat": 1.0, "fiber": 1.6,
        "sugar": 0.2, "saturated_fat": 0.3, "iron": 0.6, "calcium": 3, "magnesium": 39,
        "potassium": 86, "sodium": 4, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 9,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Quinoa, Cooked",
        "calories": 120, "protein": 4.4, "carbohydrates": 21.3, "fat": 1.9, "fiber": 2.8,
        "sugar": 0.9, "saturated_fat": 0.2, "iron": 1.5, "calcium": 17, "magnesium": 64,
        "potassium": 172, "sodium": 7, "vitamin_a": 1, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 42,
        "categories": ["protein", "carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Sweet Potato, Baked",
        "calories": 90, "protein": 2.0, "carbohydrates": 20.7, "fat": 0.2, "fiber": 3.3,
        "sugar": 6.5, "saturated_fat": 0, "iron": 0.7, "calcium": 38, "magnesium": 27,
        "potassium": 475, "sodium": 36, "vitamin_a": 961, "vitamin_c": 19.6, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 6,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Olive Oil",
        "calories": 884, "protein": 0, "carbohydrates": 0, "fat": 100, "fiber": 0,
        "sugar": 0, "saturated_fat": 13.8, "iron": 0.6, "calcium": 1, "magnesium": 0,
        "potassium": 1, "sodium": 2, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 0,
        "categories": ["fat"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Avocado",
        "calories": 160, "protein": 2.0, "carbohydrates": 8.5, "fat": 14.7, "fiber": 6.7,
        "sugar": 0.7, "saturated_fat": 2.1, "iron": 0.6, "calcium": 12, "magnesium": 29,
        "potassium": 485, "sodium": 7, "vitamin_a": 7, "vitamin_c": 10, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 81,
        "categories": ["fat", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Almonds",
        "calories": 579, "protein": 21.2, "carbohydrates": 21.6, "fat": 49.9, "fiber": 12.5,
        "sugar": 4.4, "saturated_fat": 3.8, "iron": 3.7, "calcium": 269, "magnesium": 270,
        "potassium": 733, "sodium": 1, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 44,
        "categories": ["protein", "fat", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Broccoli, Cooked",
        "calories": 35, "protein": 2.4, "carbohydrates": 7.2, "fat": 0.4, "fiber": 3.3,
        "sugar": 1.4, "saturated_fat": 0.1, "iron": 0.7, "calcium": 40, "magnesium": 21,
        "potassium": 293, "sodium": 41, "vitamin_a": 77, "vitamin_c": 64.9, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 108,
        "categories": ["fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },

    # ----------------------------------------------------
    # NEW EXPANDED FOODS (PROTEIN, FATS, CARBS, FIBER)
    # ----------------------------------------------------
    # PROTEIN RICH (Poultry, Meat, Seafood, Dairy, Plant)
    {
        "name": "Turkey Breast, Cooked",
        "calories": 135, "protein": 30.1, "carbohydrates": 0.0, "fat": 0.7, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 0.2, "iron": 1.4, "calcium": 21, "magnesium": 28,
        "potassium": 298, "sodium": 63, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0.1,
        "vitamin_b12": 0.4, "folate": 9,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Canned Tuna in Water, Drained",
        "calories": 116, "protein": 25.5, "carbohydrates": 0.0, "fat": 0.8, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 0.2, "iron": 1.5, "calcium": 11, "magnesium": 27,
        "potassium": 237, "sodium": 338, "vitamin_a": 18, "vitamin_c": 0, "vitamin_d": 2.0,
        "vitamin_b12": 2.5, "folate": 4,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Canned Tuna in Oil, Drained",
        "calories": 198, "protein": 29.1, "carbohydrates": 0.0, "fat": 8.2, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 1.4, "iron": 1.4, "calcium": 13, "magnesium": 31,
        "potassium": 250, "sodium": 354, "vitamin_a": 20, "vitamin_c": 0, "vitamin_d": 1.7,
        "vitamin_b12": 2.2, "folate": 5,
        "categories": ["protein", "fat"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Lean Beef Steak (85% Lean), Cooked",
        "calories": 215, "protein": 26.2, "carbohydrates": 0.0, "fat": 11.5, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 4.5, "iron": 2.6, "calcium": 18, "magnesium": 21,
        "potassium": 330, "sodium": 66, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0.1,
        "vitamin_b12": 2.6, "folate": 9,
        "categories": ["protein", "fat"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Shrimp, Cooked",
        "calories": 99, "protein": 24.0, "carbohydrates": 0.2, "fat": 0.3, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 0.1, "iron": 0.2, "calcium": 70, "magnesium": 39,
        "potassium": 259, "sodium": 111, "vitamin_a": 54, "vitamin_c": 0, "vitamin_d": 0.1,
        "vitamin_b12": 1.2, "folate": 3,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Cottage Cheese, Low Fat (2%)",
        "calories": 81, "protein": 11.0, "carbohydrates": 4.7, "fat": 2.3, "fiber": 0.0,
        "sugar": 4.0, "saturated_fat": 1.2, "iron": 0.1, "calcium": 111, "magnesium": 9,
        "potassium": 125, "sodium": 321, "vitamin_a": 37, "vitamin_c": 0, "vitamin_d": 0.1,
        "vitamin_b12": 0.5, "folate": 12,
        "categories": ["protein"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Egg Whites, Cooked",
        "calories": 52, "protein": 10.9, "carbohydrates": 0.7, "fat": 0.2, "fiber": 0.0,
        "sugar": 0.7, "saturated_fat": 0.0, "iron": 0.1, "calcium": 7, "magnesium": 11,
        "potassium": 163, "sodium": 166, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0.1, "folate": 4,
        "categories": ["protein"],
        "preferences": ["vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Whey Protein Powder",
        "calories": 370, "protein": 80.0, "carbohydrates": 6.0, "fat": 3.0, "fiber": 0.0,
        "sugar": 2.0, "saturated_fat": 1.5, "iron": 1.0, "calcium": 450, "magnesium": 60,
        "potassium": 500, "sodium": 160, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 1.5, "folate": 10,
        "categories": ["protein"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Soy Milk, Unsweetened",
        "calories": 33, "protein": 2.8, "carbohydrates": 1.6, "fat": 1.6, "fiber": 0.5,
        "sugar": 0.6, "saturated_fat": 0.2, "iron": 0.6, "calcium": 120, "magnesium": 15,
        "potassium": 120, "sodium": 38, "vitamin_a": 45, "vitamin_c": 0, "vitamin_d": 1.2,
        "vitamin_b12": 1.1, "folate": 16,
        "categories": ["protein"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Edamame, Steamed",
        "calories": 122, "protein": 11.9, "carbohydrates": 8.9, "fat": 5.2, "fiber": 5.2,
        "sugar": 2.2, "saturated_fat": 0.6, "iron": 2.3, "calcium": 63, "magnesium": 64,
        "potassium": 436, "sodium": 6, "vitamin_a": 15, "vitamin_c": 6.1, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 303,
        "categories": ["protein", "fat", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Tempeh",
        "calories": 192, "protein": 20.3, "carbohydrates": 7.6, "fat": 10.8, "fiber": 4.8,
        "sugar": 0.0, "saturated_fat": 2.2, "iron": 2.7, "calcium": 111, "magnesium": 81,
        "potassium": 412, "sodium": 9, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 24,
        "categories": ["protein", "fat", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Seitan (Wheat Gluten)",
        "calories": 370, "protein": 75.0, "carbohydrates": 14.0, "fat": 1.9, "fiber": 1.5,
        "sugar": 0.0, "saturated_fat": 0.3, "iron": 5.2, "calcium": 142, "magnesium": 25,
        "potassium": 100, "sodium": 1000, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 0,
        "categories": ["protein"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Cod Fish, Baked",
        "calories": 105, "protein": 23.0, "carbohydrates": 0.0, "fat": 0.9, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 0.2, "iron": 0.4, "calcium": 16, "magnesium": 32,
        "potassium": 413, "sodium": 78, "vitamin_a": 12, "vitamin_c": 0, "vitamin_d": 0.9,
        "vitamin_b12": 0.9, "folate": 7,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Sardines in Oil, Canned",
        "calories": 208, "protein": 24.6, "carbohydrates": 0.0, "fat": 11.5, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 1.5, "iron": 2.9, "calcium": 382, "magnesium": 39,
        "potassium": 397, "sodium": 505, "vitamin_a": 32, "vitamin_c": 0, "vitamin_d": 4.8,
        "vitamin_b12": 8.9, "folate": 10,
        "categories": ["protein", "fat"],
        "preferences": ["gluten_free", "lactose_free"],
    },
    {
        "name": "Pork Tenderloin, Cooked",
        "calories": 143, "protein": 26.0, "carbohydrates": 0.0, "fat": 3.5, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 1.2, "iron": 1.2, "calcium": 6, "magnesium": 28,
        "potassium": 421, "sodium": 53, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0.6,
        "vitamin_b12": 0.6, "folate": 4,
        "categories": ["protein"],
        "preferences": ["gluten_free", "lactose_free"],
    },

    # FATS RICH (Nuts, Oils, Seeds, Cheeses, Butter)
    {
        "name": "Walnuts",
        "calories": 654, "protein": 15.2, "carbohydrates": 13.7, "fat": 65.2, "fiber": 6.7,
        "sugar": 2.6, "saturated_fat": 6.1, "iron": 2.9, "calcium": 98, "magnesium": 158,
        "potassium": 441, "sodium": 2, "vitamin_a": 1, "vitamin_c": 1.3, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 98,
        "categories": ["fat", "protein", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Peanut Butter, Natural",
        "calories": 588, "protein": 25.1, "carbohydrates": 20.0, "fat": 50.4, "fiber": 6.0,
        "sugar": 9.2, "saturated_fat": 10.3, "iron": 1.9, "calcium": 43, "magnesium": 154,
        "potassium": 649, "sodium": 17, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 92,
        "categories": ["fat", "protein", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Chia Seeds",
        "calories": 486, "protein": 16.5, "carbohydrates": 42.1, "fat": 30.7, "fiber": 34.4,
        "sugar": 0.0, "saturated_fat": 3.3, "iron": 7.7, "calcium": 631, "magnesium": 335,
        "potassium": 407, "sodium": 16, "vitamin_a": 2, "vitamin_c": 1.6, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 49,
        "categories": ["fat", "fiber", "protein"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Flaxseeds, Ground",
        "calories": 534, "protein": 18.3, "carbohydrates": 28.9, "fat": 42.2, "fiber": 27.3,
        "sugar": 1.6, "saturated_fat": 3.7, "iron": 5.7, "calcium": 255, "magnesium": 392,
        "potassium": 813, "sodium": 30, "vitamin_a": 0, "vitamin_c": 0.6, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 87,
        "categories": ["fat", "fiber", "protein"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Pumpkin Seeds, Roasted",
        "calories": 574, "protein": 29.8, "carbohydrates": 14.7, "fat": 49.1, "fiber": 6.5,
        "sugar": 1.3, "saturated_fat": 8.7, "iron": 8.8, "calcium": 52, "magnesium": 592,
        "potassium": 809, "sodium": 7, "vitamin_a": 1, "vitamin_c": 1.9, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 58,
        "categories": ["fat", "protein", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Cheddar Cheese",
        "calories": 403, "protein": 24.9, "carbohydrates": 1.3, "fat": 33.1, "fiber": 0.0,
        "sugar": 0.5, "saturated_fat": 21.1, "iron": 0.7, "calcium": 721, "magnesium": 28,
        "potassium": 98, "sodium": 621, "vitamin_a": 265, "vitamin_c": 0, "vitamin_d": 0.6,
        "vitamin_b12": 0.8, "folate": 18,
        "categories": ["fat", "protein"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Parmesan Cheese",
        "calories": 431, "protein": 38.5, "carbohydrates": 4.1, "fat": 28.6, "fiber": 0.0,
        "sugar": 0.9, "saturated_fat": 17.1, "iron": 0.9, "calcium": 1184, "magnesium": 44,
        "potassium": 152, "sodium": 1529, "vitamin_a": 207, "vitamin_c": 0, "vitamin_d": 0.5,
        "vitamin_b12": 1.2, "folate": 7,
        "categories": ["protein", "fat"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Feta Cheese",
        "calories": 264, "protein": 14.2, "carbohydrates": 4.1, "fat": 21.3, "fiber": 0.0,
        "sugar": 4.1, "saturated_fat": 14.9, "iron": 0.7, "calcium": 493, "magnesium": 19,
        "potassium": 62, "sodium": 1116, "vitamin_a": 125, "vitamin_c": 0, "vitamin_d": 0.4,
        "vitamin_b12": 1.7, "folate": 32,
        "categories": ["fat", "protein"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Butter, Unsalted",
        "calories": 717, "protein": 0.9, "carbohydrates": 0.1, "fat": 81.1, "fiber": 0.0,
        "sugar": 0.1, "saturated_fat": 51.4, "iron": 0.0, "calcium": 24, "magnesium": 2,
        "potassium": 24, "sodium": 11, "vitamin_a": 684, "vitamin_c": 0, "vitamin_d": 1.5,
        "vitamin_b12": 0.2, "folate": 3,
        "categories": ["fat"],
        "preferences": ["vegetarian", "gluten_free"],
    },
    {
        "name": "Coconut Oil",
        "calories": 862, "protein": 0.0, "carbohydrates": 0.0, "fat": 100.0, "fiber": 0.0,
        "sugar": 0.0, "saturated_fat": 86.5, "iron": 0.1, "calcium": 0, "magnesium": 0,
        "potassium": 0, "sodium": 0, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 0,
        "categories": ["fat"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Tahini (Sesame Paste)",
        "calories": 595, "protein": 17.0, "carbohydrates": 21.2, "fat": 53.7, "fiber": 9.3,
        "sugar": 0.5, "saturated_fat": 7.5, "iron": 9.0, "calcium": 426, "magnesium": 95,
        "potassium": 414, "sodium": 115, "vitamin_a": 2, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 98,
        "categories": ["fat", "protein", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Dark Chocolate (70-85% Cacao)",
        "calories": 598, "protein": 7.8, "carbohydrates": 45.9, "fat": 42.6, "fiber": 10.9,
        "sugar": 24.0, "saturated_fat": 24.5, "iron": 11.9, "calcium": 73, "magnesium": 228,
        "potassium": 715, "sodium": 20, "vitamin_a": 2, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0.3, "folate": 10,
        "categories": ["fat", "carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Cashews, Dry Roasted",
        "calories": 574, "protein": 15.3, "carbohydrates": 32.7, "fat": 46.4, "fiber": 3.0,
        "sugar": 5.0, "saturated_fat": 9.2, "iron": 6.0, "calcium": 45, "magnesium": 273,
        "potassium": 565, "sodium": 16, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 69,
        "categories": ["fat", "protein"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Pecan Nuts",
        "calories": 691, "protein": 9.2, "carbohydrates": 13.9, "fat": 72.0, "fiber": 9.6,
        "sugar": 4.0, "saturated_fat": 6.2, "iron": 2.5, "calcium": 70, "magnesium": 121,
        "potassium": 410, "sodium": 0, "vitamin_a": 3, "vitamin_c": 1.1, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 22,
        "categories": ["fat", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },

    # CARBOHYDRATES RICH (Grains, Breads, Pasta, Starchy Veggies, Fruits)
    {
        "name": "White Rice, Cooked",
        "calories": 130, "protein": 2.7, "carbohydrates": 28.2, "fat": 0.3, "fiber": 0.4,
        "sugar": 0.1, "saturated_fat": 0.1, "iron": 1.2, "calcium": 10, "magnesium": 12,
        "potassium": 35, "sodium": 1, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 58,
        "categories": ["carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Whole Wheat Bread",
        "calories": 247, "protein": 13.0, "carbohydrates": 41.3, "fat": 3.4, "fiber": 6.0,
        "sugar": 5.6, "saturated_fat": 0.7, "iron": 2.5, "calcium": 161, "magnesium": 75,
        "potassium": 250, "sodium": 450, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 50,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Whole Wheat Pasta, Cooked",
        "calories": 124, "protein": 5.3, "carbohydrates": 26.5, "fat": 0.5, "fiber": 3.9,
        "sugar": 0.8, "saturated_fat": 0.1, "iron": 1.5, "calcium": 15, "magnesium": 42,
        "potassium": 118, "sodium": 3, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 18,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Banana",
        "calories": 89, "protein": 1.1, "carbohydrates": 22.8, "fat": 0.3, "fiber": 2.6,
        "sugar": 12.2, "saturated_fat": 0.1, "iron": 0.3, "calcium": 5, "magnesium": 27,
        "potassium": 358, "sodium": 1, "vitamin_a": 3, "vitamin_c": 8.7, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 20,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Apple with Skin",
        "calories": 52, "protein": 0.3, "carbohydrates": 13.8, "fat": 0.2, "fiber": 2.4,
        "sugar": 10.4, "saturated_fat": 0.0, "iron": 0.1, "calcium": 6, "magnesium": 5,
        "potassium": 107, "sodium": 1, "vitamin_a": 3, "vitamin_c": 4.6, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 3,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "White Potato, Baked with Skin",
        "calories": 93, "protein": 2.5, "carbohydrates": 21.2, "fat": 0.1, "fiber": 2.2,
        "sugar": 1.2, "saturated_fat": 0.0, "iron": 1.1, "calcium": 15, "magnesium": 28,
        "potassium": 535, "sodium": 10, "vitamin_a": 0, "vitamin_c": 12.6, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 28,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Couscous, Cooked",
        "calories": 112, "protein": 3.8, "carbohydrates": 23.2, "fat": 0.2, "fiber": 1.4,
        "sugar": 0.1, "saturated_fat": 0.0, "iron": 0.4, "calcium": 8, "magnesium": 8,
        "potassium": 58, "sodium": 5, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 15,
        "categories": ["carbohydrates"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Rolled Oats, Cooked",
        "calories": 71, "protein": 2.5, "carbohydrates": 12.0, "fat": 1.5, "fiber": 1.7,
        "sugar": 0.3, "saturated_fat": 0.2, "iron": 0.9, "calcium": 9, "magnesium": 27,
        "potassium": 61, "sodium": 2, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 11,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "lactose_free"],
    },
    {
        "name": "Blueberries, Fresh",
        "calories": 57, "protein": 0.7, "carbohydrates": 14.5, "fat": 0.3, "fiber": 2.4,
        "sugar": 9.9, "saturated_fat": 0.0, "iron": 0.3, "calcium": 6, "magnesium": 6,
        "potassium": 77, "sodium": 1, "vitamin_a": 3, "vitamin_c": 9.7, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 6,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Dates, Medjool",
        "calories": 277, "protein": 1.8, "carbohydrates": 75.0, "fat": 0.2, "fiber": 6.7,
        "sugar": 66.5, "saturated_fat": 0.0, "iron": 0.9, "calcium": 64, "magnesium": 54,
        "potassium": 696, "sodium": 1, "vitamin_a": 7, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 19,
        "categories": ["carbohydrates", "fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },

    # FIBER RICH (Beans, Vegetables, Seeds, Fruits)
    {
        "name": "Black Beans, Cooked",
        "calories": 132, "protein": 8.9, "carbohydrates": 23.7, "fat": 0.5, "fiber": 8.7,
        "sugar": 0.3, "saturated_fat": 0.1, "iron": 2.1, "calcium": 27, "magnesium": 60,
        "potassium": 355, "sodium": 2, "vitamin_a": 0, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 149,
        "categories": ["fiber", "protein", "carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Kidney Beans, Cooked",
        "calories": 127, "protein": 8.7, "carbohydrates": 22.8, "fat": 0.5, "fiber": 6.4,
        "sugar": 0.3, "saturated_fat": 0.1, "iron": 2.9, "calcium": 28, "magnesium": 42,
        "potassium": 405, "sodium": 2, "vitamin_a": 0, "vitamin_c": 1.2, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 130,
        "categories": ["fiber", "protein", "carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Brussels Sprouts, Cooked",
        "calories": 36, "protein": 2.6, "carbohydrates": 7.1, "fat": 0.5, "fiber": 2.6,
        "sugar": 1.7, "saturated_fat": 0.1, "iron": 1.2, "calcium": 36, "magnesium": 20,
        "potassium": 317, "sodium": 21, "vitamin_a": 38, "vitamin_c": 62.0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 61,
        "categories": ["fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Carrots, Raw",
        "calories": 41, "protein": 0.9, "carbohydrates": 9.6, "fat": 0.2, "fiber": 2.8,
        "sugar": 4.7, "saturated_fat": 0.0, "iron": 0.3, "calcium": 33, "magnesium": 12,
        "potassium": 320, "sodium": 69, "vitamin_a": 835, "vitamin_c": 5.9, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 19,
        "categories": ["fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Raspberries, Fresh",
        "calories": 52, "protein": 1.2, "carbohydrates": 11.9, "fat": 0.7, "fiber": 6.5,
        "sugar": 4.4, "saturated_fat": 0.0, "iron": 0.7, "calcium": 25, "magnesium": 22,
        "potassium": 151, "sodium": 1, "vitamin_a": 2, "vitamin_c": 26.2, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 21,
        "categories": ["fiber", "carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Artichoke, Cooked",
        "calories": 53, "protein": 2.9, "carbohydrates": 11.9, "fat": 0.3, "fiber": 5.4,
        "sugar": 1.0, "saturated_fat": 0.1, "iron": 0.6, "calcium": 21, "magnesium": 42,
        "potassium": 286, "sodium": 72, "vitamin_a": 1, "vitamin_c": 7.4, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 89,
        "categories": ["fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Pear with Skin",
        "calories": 57, "protein": 0.4, "carbohydrates": 15.2, "fat": 0.1, "fiber": 3.1,
        "sugar": 9.8, "saturated_fat": 0.0, "iron": 0.2, "calcium": 9, "magnesium": 7,
        "potassium": 116, "sodium": 1, "vitamin_a": 1, "vitamin_c": 4.3, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 7,
        "categories": ["fiber", "carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Green Peas, Cooked",
        "calories": 84, "protein": 5.4, "carbohydrates": 15.6, "fat": 0.4, "fiber": 5.5,
        "sugar": 5.9, "saturated_fat": 0.1, "iron": 1.5, "calcium": 27, "magnesium": 36,
        "potassium": 271, "sodium": 3, "vitamin_a": 38, "vitamin_c": 14.2, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 65,
        "categories": ["fiber", "protein", "carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Spinach, Cooked",
        "calories": 23, "protein": 3.0, "carbohydrates": 3.8, "fat": 0.3, "fiber": 2.4,
        "sugar": 0.4, "saturated_fat": 0.0, "iron": 3.6, "calcium": 136, "magnesium": 87,
        "potassium": 466, "sodium": 126, "vitamin_a": 524, "vitamin_c": 9.8, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 146,
        "categories": ["fiber"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    },
    {
        "name": "Popcorn, Air-Popped",
        "calories": 387, "protein": 12.9, "carbohydrates": 77.9, "fat": 4.5, "fiber": 14.5,
        "sugar": 0.9, "saturated_fat": 0.6, "iron": 3.2, "calcium": 7, "magnesium": 144,
        "potassium": 329, "sodium": 7, "vitamin_a": 10, "vitamin_c": 0, "vitamin_d": 0,
        "vitamin_b12": 0, "folate": 31,
        "categories": ["fiber", "carbohydrates"],
        "preferences": ["vegan", "vegetarian", "gluten_free", "lactose_free"],
    }
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