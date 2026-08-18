from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base

__test__ = False


class TestRun(Base):
    __tablename__ = "test_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    change_id: Mapped[int] = mapped_column(
        ForeignKey("api_changes.id", ondelete="CASCADE"),
        nullable=False
    )
    passed: Mapped[bool] = mapped_column(Boolean, nullable=False)
    exit_code: Mapped[int] = mapped_column(Integer, nullable=False)
    output: Mapped[str] = mapped_column(Text, nullable=False)
    duration_seconds: Mapped[float] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )