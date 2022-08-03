from .base import Base
from .mixins import TimestampMixin
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Integer
from .post_tag import posts_tags_table


class Post(Base, TimestampMixin):
    name = Column(String(20), default="")
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False, unique=False)
    title = Column(String, default="")
    author = relationship("Author", back_populates="post")
    tag = relationship("Tag", secondary=posts_tags_table, back_populates="post")

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.name)
