from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Enum,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.models.enums import (
    ActivityLevel,
    TargetMode,
    UserGoal,
    LifeStage,
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    weight_kg: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    height_cm: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    activity_level: Mapped[ActivityLevel] = mapped_column(
        Enum(
            ActivityLevel,
            name="activity_level_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    goal: Mapped[UserGoal] = mapped_column(
        Enum(
            UserGoal,
            name="user_goal_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    target_mode: Mapped[TargetMode] = mapped_column(
        Enum(
            TargetMode,
            name="target_mode_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        default=TargetMode.CALCULATED,
        nullable=False,
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

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    targets: Mapped["UserTarget | None"] = relationship(
        "UserTarget",
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
    )

    preferences: Mapped[list["UserPreference"]] = relationship(
        "UserPreference",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    favorite_recipes: Mapped[list["FavoriteRecipe"]] = relationship(
        "FavoriteRecipe",
        back_populates="user",
        cascade="all, delete-orphan",
    )


    life_stage: Mapped[LifeStage] = mapped_column(
        Enum(
            LifeStage,
            name="life_stage_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        default=LifeStage.STANDARD,
        nullable=False,
    )
    