from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.enums import PeriodEnum
from app.models.base import Base


class Habit(Base):
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    periodicity = Column(
        Enum(PeriodEnum, name="period_enum"),
        nullable=False,
        default=PeriodEnum.DAILY,
    )
    reminder_time = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="habits")

    def __repr__(self):
        return f"Habit: {self.title}"
