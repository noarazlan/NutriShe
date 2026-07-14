from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.models.enums import FoodCategoryType


class Food(Base):
    __tablename__ = "foods"

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

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    calories_per_100g: Mapped[Decimal] = mapped_column(
        Numeric(8, 2),
        nullable=False,
    )

    protein_per_100g: Mapped[Decimal] = mapped_column(
        Numeric(7, 2),
        nullable=False,
    )

    carbohydrates_per_100g: Mapped[Decimal] = mapped_column(
        Numeric(7, 2),
        nullable=False,
    )

    fat_per_100g: Mapped[Decimal] = mapped_column(
        Numeric(7, 2),
        nullable=False,
    )

    fiber_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    sugar_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    saturated_fat_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    iron_mg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(8, 3),
        nullable=True,
    )

    calcium_mg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    magnesium_mg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    potassium_mg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    sodium_mg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    vitamin_a_mcg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    vitamin_c_mg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    vitamin_d_mcg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 3),
        nullable=True,
    )

    vitamin_b12_mcg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 3),
        nullable=True,
    )

    folate_mcg_per_100g: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    data_source: Mapped[str | None] = mapped_column(
        String(255),
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

    categories: Mapped[list["FoodCategory"]] = relationship(
        "FoodCategory",
        back_populates="food",
        cascade="all, delete-orphan",
    )

    preferences: Mapped[list["FoodPreference"]] = relationship(
        "FoodPreference",
        back_populates="food",
        cascade="all, delete-orphan",
    )


class FoodCategory(Base):
    __tablename__ = "food_categories"

    food_id: Mapped[int] = mapped_column(
        ForeignKey(
            "foods.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    category: Mapped[FoodCategoryType] = mapped_column(
        Enum(
            FoodCategoryType,
            name="food_category_type_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        primary_key=True,
    )

    food: Mapped["Food"] = relationship(
        "Food",
        back_populates="categories",
    )


class FoodPreference(Base):
    __tablename__ = "food_preferences"

    food_id: Mapped[int] = mapped_column(
        ForeignKey(
            "foods.id",
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

    food: Mapped["Food"] = relationship(
        "Food",
        back_populates="preferences",
    )

    preference: Mapped["Preference"] = relationship(
        "Preference",
        back_populates="foods",
    )