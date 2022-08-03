"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
)

from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    scoped_session,
    sessionmaker,
    relationship
)


import os

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)

session_factory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
Base = declarative_base(bind=engine, cls=Base)
Session = scoped_session(session_factory)


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, default=None, unique=False)
    username = Column(String, default=None, unique=True)
    email = Column(String, default=None, unique=True)
    post = relationship('Post', back_populates='user')


class Post(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=False)
    title = Column(String, default=None, unique=False)
    body = Column(String, default=None, unique=False)
    user = relationship('User', back_populates='post')



