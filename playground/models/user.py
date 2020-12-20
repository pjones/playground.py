from dataclasses import dataclass
from playground.database import Base
from playground.models.address import Address
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from typing import List


@dataclass
class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(Text, unique=True)
    addresses: List[Address] = relationship("Address")

    def __init__(self, name):
        self.name = name
