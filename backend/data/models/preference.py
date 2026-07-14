from __future__ import annotations

from sqlalchemy import Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.models.enums import PreferenceType


class Preference(Base):
    __tablename__ = "preferences"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    preference_type: Mapped[PreferenceType] = mapped_column(
        Enum(
            PreferenceType,
            name="preference_type_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    users: Mapped[list["UserPreference"]] = relationship(
        "UserPreference",
        back_populates="preference",
        cascade="all, delete-orphan",
    )

    foods: Mapped[list["FoodPreference"]] = relationship(
        "FoodPreference",
        back_populates="preference",
        cascade="all, delete-orphan",
    )

    recipes: Mapped[list["RecipePreference"]] = relationship(
        "RecipePreference",
        back_populates="preference",
        cascade="all, delete-orphan",
    )

    tips: Mapped[list["TipPreference"]] = relationship(
        "TipPreference",
        back_populates="preference",
        cascade="all, delete-orphan",
    )


class UserPreference(Base):
    __tablename__ = "user_preferences"

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
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

    user: Mapped["User"] = relationship(
        "User",
        back_populates="preferences",
    )

    preference: Mapped["Preference"] = relationship(
        "Preference",
        back_populates="users",
    )