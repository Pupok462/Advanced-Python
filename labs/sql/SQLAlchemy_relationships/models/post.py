from .base import Base
from .mixins import TimestampMixin
from sqlalchemy.orm import relationship

from sqlalchemy import Column, String, ForeignKey, Integer


class Post(Base, TimestampMixin):
    name = Column(String(20), default="")
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False, unique=False)
    title = Column(String, default="")
    author = relationship("Author", back_populates="post")
