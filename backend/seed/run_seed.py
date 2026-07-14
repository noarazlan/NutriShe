import data.models  # noqa: F401

from data.database import SessionLocal
from seed.seed_foods import seed_foods
from seed.seed_preferences import seed_preferences
from seed.seed_recipes import seed_recipes
from seed.seed_reference_values import seed_reference_values
from seed.seed_tips import seed_tips


def run_seed() -> None:
    db = SessionLocal()

    try:
        seed_preferences(db)
        print("Preferences seeded successfully.")

        seed_reference_values(db)
        print("Nutrient reference values seeded successfully.")

        seed_foods(db)
        print("Foods seeded successfully.")

        seed_recipes(db)
        print("Recipes seeded successfully.")

        seed_tips(db)
        print("Tips seeded successfully.")

        print("All seed data was inserted successfully.")

    except Exception as error:
        db.rollback()
        print(f"Seeding failed: {error}")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    run_seed()