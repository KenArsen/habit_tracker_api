from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql import func


class BaseModelMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime(timezone=True), default=func.now, onupdate=func.now())
