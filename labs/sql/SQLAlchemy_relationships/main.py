from models.base import Base, Session
from models import User, Author, Post
from sqlalchemy.orm import Session as SessionType, joinedload


def create_user(
    session: SessionType, username: str, priority: bool, e_mail: str
) -> User:
    user = User(username=username, priority=priority, e_mail=e_mail)
    print("Created user", user)
    session.add(user)
    session.commit()
    print("created user", user)

    return user


def create_table():
    Base.metadata.create_all()


def fetch_author_by_id(session: SessionType, author_id: int) -> Author:
    author: Author = session.get(Author, author_id, options=(joinedload(Author.user),))

    print(author)
    print(Author.user)

    return author


def create_author_for_user(
    session: SessionType, user: User, author_name: str
) -> Author:
    author = Author(name=author_name, user=user)
    print("create author", author)
    session.add(author)
    session.commit()
    print("created author", author)
    return author


def create_post_by_author(session: SessionType, author: Author, post: str) -> Post:
    post = Post(title=post, author=author)
    session.add(post)
    session.commit()
    return author


def drop_table():
    """
    SQL_CODE
    DROP TABLE workers
    """
    Base.metadata.drop_all()


def main():

    # create_table()
    # drop_table()
    session: SessionType = Session()
    user = create_user(session, username="Sir", e_mail="sir@gmail.com", priority=False)
    author = create_author_for_user(session, author_name="Adamian", user=user)
    post = create_post_by_author(session, post="About life", author=author)
    fetch_author_by_id(session, author_id=2)
    session.close()


if __name__ == "__main__":
    main()
