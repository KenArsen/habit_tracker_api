from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declared_attr


class BaseModelMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=datetime.utcnow)

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
