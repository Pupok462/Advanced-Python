from .base import Base
from .mixins import TimestampMixin
from sqlalchemy.orm import relationship

from sqlalchemy import Column, String
from .post_tag import posts_tags_table


class Tag(Base, TimestampMixin):

    name = Column(String, unique=True)
    post = relationship("Post", secondary=posts_tags_table, back_populates="tag")

    def __str__(self):
        return self.name

    def __repr__(self):
        return repr(self.name)