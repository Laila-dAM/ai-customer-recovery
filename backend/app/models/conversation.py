from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
        index=True,
    )

    lead_id: Mapped[int] = mapped_column(
        ForeignKey("leads.id"),
        nullable=False,
        index=True,
    )

    channel: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="whatsapp",
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="open",
        index=True,
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

    company: Mapped["Company"] = relationship()
    lead: Mapped["Lead"] = relationship()
    messages: Mapped[list["Message"]] = relationship(back_populates="conversation", cascade="all, delete-orphan")
