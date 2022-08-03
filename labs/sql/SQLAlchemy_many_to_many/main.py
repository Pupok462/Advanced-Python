from models.base import Base, Session
from models import User, Author, Post, Tag
from sqlalchemy.orm import Session as SessionType, joinedload


def create_all_tables():
    Base.metadata.create_all()


def drop_all_tables():
    Base.metadata.drop_all()


def create_user(session: SessionType, name: str, priority: bool) -> User:
    user = User(username=name, priority=priority)
    session.add(user)
    session.commit()


def create_author_by_user_id(session: SessionType, user_id: int, name: str) -> Author:
    author = Author(user_id=user_id, name=name)
    session.add(author)
    session.commit()


def create_posts_by_author_id(session: SessionType, author_id: int, name: str) -> Post:
    post = Post(author_id=author_id, name=name)
    session.add(post)
    session.commit()


def create_tags(session: SessionType, *tags_name: str):
    tags = []
    for tag_name in tags_name:
        tag = Tag(name=tag_name)
        tags.append(tag.name)
        session.add(tag)
    session.commit()
    print('Created tags', tags)


def show_all_post_for_each_author(session: SessionType):
    authors: list[Author] = (
        session.query(Author)
        .options(joinedload(Author.post))
    )
    for author in authors:
        if len(author.post) == 0:
            print("Author", author.id, author.name)
            print("-- posts", "No posts")
        else:
            print("Author", author.id, author.name)
            print("-- posts", author.post)


def delete_some_tag_by_name(session: SessionType, tag_name: str):
    tags: list[Tag] = session.query(Tag).all()
    for tag in tags:
        if tag_name in tag.name:
            session.delete(tag)
            # TODO: понять почему ValueError не работает
        else:
            ValueError("Tag not found")
    session.commit()


def connect_tags_with_posts(session: SessionType):
    tags: list[Tag] = session.query(Tag).all()
    posts: list[Post] = session.query(Post).all()

    for tag in tags:
        for post in posts:
            if tag.name in post.name.lower():
                post.tag.append(tag)
    session.commit()


def find_user_by_username(session: SessionType, username: str) -> User:
    user = session.query(User).filter_by(username=username).one_or_none()
    return user


def show_all_post_with_tags(session: SessionType):
    posts: list[Post] = (
        session.query(Post)
        .options(joinedload(Post.tag))
    )
    for post in posts:
        if len(post.tag) == 0:
            print("Post", post.id, post.name)
            print("-- Tags", "No posts")
        else:
            print("Post", post.id, post.name)
            print("-- Tags", post.tag)


def show_user_who_author_with_post_tags(session: SessionType, username: str):
    answer = (
        session.query(User.username, Author.name, Post.name, Tag.name)
        .join(User.author)
        .join(Author.post)
        .join(Post.tag)
        .filter(User.username == username)
        .one_or_none()
    )
    print("-----------Founded User -----------")
    print(f"Username - {answer[0]}")
    print(f"Author name - {answer[1]}")
    print(f"Posts - {answer[2]}")
    print(f"Tags - {answer[3]}")
    print("-----------------------------------")




def main():
    # create_all_tables()
    # drop_all_tables()
    session: SessionType = Session()
    # create_user(session, name="James", priority=True)
    # create_tags(session, "python", "news", "django", "flask", "sqlalchemy")
    # create_posts_by_author_id(session, author_id=3, name="SQLAlchemy Intro")
    # show_all_post_for_each_author(session)
    # connect_tags_with_posts(session)
    # show_all_post_with_tags(session)
    # delete_some_tag_by_name(session, "flask")
    show_user_who_author_with_post_tags(session, "Jack")
    session.close()


if __name__ == "__main__":
    main()
