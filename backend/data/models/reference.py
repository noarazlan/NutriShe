from decimal import Decimal

from sqlalchemy import Enum, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from data.base import Base
from data.models.enums import LifeStage, ReferenceType


class NutrientReferenceValue(Base):
    __tablename__ = "nutrient_reference_values"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    nutrient_code: Mapped[str] = mapped_column(
        String(50),
        index=True,
        nullable=False,
    )

    display_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    min_age: Mapped[int] = mapped_column(
        nullable=False,
    )

    max_age: Mapped[int | None] = mapped_column(
        nullable=True,
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

    recommended_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 3),
        nullable=False,
    )

    upper_limit_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 3),
        nullable=True,
    )

    reference_type: Mapped[ReferenceType] = mapped_column(
        Enum(
            ReferenceType,
            name="reference_type_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    source_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    source_year: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    source_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )