from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
