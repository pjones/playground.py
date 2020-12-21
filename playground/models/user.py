from dataclasses import dataclass
from datetime import datetime
from playground.database import Base
from playground.models.address import Address
from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func
from typing import List


@dataclass
class User(Base):
    __tablename__ = "users"

    # Columns that are automatically set by the database:
    id: int = Column(Integer, primary_key=True)
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    # Columns that are managed by SQL Alchemy:
    addresses: List[Address] = relationship("Address")

    # Other columns:
    name: str = Column(Text, unique=True, nullable=False)

    def __init__(self, name):
        """
        Create a new user with the given name.
        """
        self.name = name

    @staticmethod
    def find_by_id(db: Session, user_id: int):
        """
        Find a specific user given their database ID.
        """
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def find_by_name_and_address(db: Session, name: str, address_label: str):
        """
        Find a user that has the given name.

        The user must also have at least one address that matches the
        given label.

        Parameters
        ----------
        db : Session
          A database session
        name : str
          A user's name.
        address_label : str
          The address label to search for.
        """
        from playground.models.address import Address

        return (
            db.query(User)
            .filter(User.name == name)
            .join(Address)
            .filter(Address.label == address_label)
            .first()
        )
