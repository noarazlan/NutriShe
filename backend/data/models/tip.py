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
from data.models.enums import TipType


class Tip(Base):
    __tablename__ = "tips"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    tip_type: Mapped[TipType] = mapped_column(
        Enum(
            TipType,
            name="tip_type_enum",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        default=TipType.GENERAL,
        nullable=False,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
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

    preferences: Mapped[list["TipPreference"]] = relationship(
        "TipPreference",
        back_populates="tip",
        cascade="all, delete-orphan",
    )


class TipPreference(Base):
    __tablename__ = "tip_preferences"

    tip_id: Mapped[int] = mapped_column(
        ForeignKey(
            "tips.id",
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

    tip: Mapped["Tip"] = relationship(
        "Tip",
        back_populates="preferences",
    )

    preference: Mapped["Preference"] = relationship(
        "Preference",
        back_populates="tips",
    )