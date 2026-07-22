from __future__ import annotations

from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.models.enums import MealType


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    ingredients_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    instructions: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    preparation_time_minutes: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    servings: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    preferences: Mapped[list["RecipePreference"]] = relationship(
        "RecipePreference",
        back_populates="recipe",
        cascade="all, delete-orphan",
    )

    favorited_by: Mapped[list["FavoriteRecipe"]] = relationship(
        "FavoriteRecipe",
        back_populates="recipe",
        cascade="all, delete-orphan",
    )

    meal_types: Mapped[list["RecipeMealType"]] = relationship(
        "RecipeMealType",
        back_populates="recipe",
        cascade="all, delete-orphan",
    )


class RecipePreference(Base):
    __tablename__ = "recipe_preferences"

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey(
            "recipes.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    preference_id: Mapped[int] = mapped_column(
        ForeignKey(
            "preferences.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    recipe: Mapped["Recipe"] = relationship(
        "Recipe",
        back_populates="preferences",
    )

    preference: Mapped["Preference"] = relationship(
        "Preference",
        back_populates="recipes",
    )



class RecipeMealType(Base):
    __tablename__ = "recipe_meal_types"

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey(
            "recipes.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    meal_type: Mapped[MealType] = mapped_column(
        Enum(
            MealType,
            name="meal_type_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        primary_key=True,
    )

    recipe: Mapped["Recipe"] = relationship(
        "Recipe",
        back_populates="meal_types",
    )