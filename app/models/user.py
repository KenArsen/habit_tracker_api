from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class User(Base):
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    habits = relationship("Habit", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"User {self.email}"
