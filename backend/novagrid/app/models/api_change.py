from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.connection import Base

class ApiChange(Base):
    __tablename__ = "api_changes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_id: Mapped[int] = mapped_column(ForeignKey("api_sources.id", ondelete="CASCADE"), nullable=False)
    from_version_id: Mapped[int] = mapped_column(ForeignKey("api_versions.id"), nullable=False)
    to_version_id: Mapped[int] = mapped_column(ForeignKey("api_versions.id"), nullable=False)
    classification: Mapped[str] = mapped_column(String(50), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    changes_json: Mapped[list] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
