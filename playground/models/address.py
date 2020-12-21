from dataclasses import dataclass
from datetime import datetime
from playground.database import Base
from sqlalchemy import Column, DateTime, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func


@dataclass
class Address(Base):
    __tablename__ = "addresses"

    # Columns that are automatically set by the database:
    id: int = Column(Integer, primary_key=True)
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    # Relationships:
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    # Can't use type hints here otherwise we get circular dependencies:
    user = relationship("User", back_populates="addresses")

    # Other columns:
    label: str = Column(Text, nullable=False)
    display_text: str = Column(Text, nullable=False)

    def __init__(self, label, display_text):
        self.label = label
        self.display_text = display_text

    @staticmethod
    def find_by_user_id_and_label(db: Session, user_id: int, label: str):
        from playground.models.user import User

        return (
            db.query(Address)
            .filter(Address.label == label)
            .join(User)
            .filter(User.id == user_id)
            .first()
        )
