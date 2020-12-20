from dataclasses import dataclass
from playground.database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class Address(Base):
    __tablename__ = "addresses"

    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(Integer, ForeignKey("users.id"), nullable=False)
    label: str = Column(Text, nullable=False)
    display_text: str = Column(Text, nullable=False)

    def __init__(self, label, display_text):
        self.label = label
        self.display_text = display_text
