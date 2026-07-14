from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.base import Base
from data.models.enums import TargetSource


class UserTarget(Base):
    __tablename__ = "user_targets"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
    )

    calories_target: Mapped[Decimal | None] = mapped_column(
        Numeric(8, 2),
        nullable=True,
    )

    protein_target_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    fat_target_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    carbohydrates_target_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    fiber_target_g: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    iron_target_mg: Mapped[Decimal | None] = mapped_column(
        Numeric(8, 2),
        nullable=True,
    )

    calcium_target_mg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    magnesium_target_mg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    potassium_target_mg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    sodium_target_mg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    vitamin_a_target_mcg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    vitamin_c_target_mg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    vitamin_d_target_mcg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 3),
        nullable=True,
    )

    vitamin_b12_target_mcg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 3),
        nullable=True,
    )

    folate_target_mcg: Mapped[Decimal | None] = mapped_column(
        Numeric(9, 2),
        nullable=True,
    )

    target_source: Mapped[TargetSource] = mapped_column(
        Enum(
            TargetSource,
            name="target_source_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        default=TargetSource.CALCULATED,
        nullable=False,
    )

    calculation_method: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="targets",
    )