from .base import Base
from .mixins import TimestampMixin
from sqlalchemy.orm import relationship

from sqlalchemy import Column, String, ForeignKey, Integer


class Author(Base, TimestampMixin):
    name = Column(String(20), unique=True, default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    books = Column(String, default="")
    post = relationship("Post", back_populates="author")
    user = relationship("User", back_populates="author")

    def __str__(self):
        return (
            f" {self.id} |"
            f" {self.name!r} |"
            f" {self.user_id} |"
            f"    {self.books}      |"
        )
