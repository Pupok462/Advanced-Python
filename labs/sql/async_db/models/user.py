from .base import Base
from .mixins import TimestampMixin
from sqlalchemy.orm import relationship


from sqlalchemy import Column, String, Boolean


class User(TimestampMixin, Base):
    username = Column(String(20), unique=True)
    priority = Column(Boolean, default=None, server_default="FALSE")
    e_mail = Column(String(70), default=None)
    author = relationship("Author", back_populates="user")

    def __str__(self):
        return (
            f" {self.id} |"
            f" {self.username!r} |"
            f" {self.e_mail} |"
            f"    {self.priority}      |"
            f" {self.created_at} |"
        )
