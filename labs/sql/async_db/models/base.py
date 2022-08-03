from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    scoped_session,
    sessionmaker,
)
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
)

import config


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> users
        """
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


engine = create_engine(url=config.SQLALCHEMY_DB_URL, echo=config.SQLALCHEMY_ECHO)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
