from sqlalchemy import Column, String

from src.db.session import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

    def __str__(self):
        return f"<User {self.email}>"
