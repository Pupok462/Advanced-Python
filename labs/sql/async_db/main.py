import asyncio
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.result import Result
import config
from models.base import Base
from models import User, Author, Post, Tag
import sys


async_engine = create_async_engine(
    config.SQLALCHEMY_ASYNC_DB_URI,
    echo=True,
)
async_session = sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_tables():

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user_by_username(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print('Created user', user)
    await session.refresh(user)
    print(" Refreshed user", user)
    return user


async def create_author_for_user_by_username(
    session: AsyncSession, username: str, name: str
) -> Author:
    query = select(User).where(User.username == username)
    result: Result = await session.execute(query)
    user: User = result.scalar_one()

    print("founded user by username", user)
    author = Author(name=name, user=user)
    session.add(author)
    print("created author", author, "for user", user)
    await session.commit()

    return author


async def create_posts_for_user(session: AsyncSession, username: str, *post_titles: str) -> list[Post]:
    query = select(Author).join(Author.user).where(User.username == username)
    result: Result = await session.execute(query)
    author: Author = result.scalar_one()

    posts = []
    for post_title in post_titles:
        post = Post(name=post_title, author=author)
        posts.append(post)

    session.add_all(posts)
    await session.commit()

    print('created posts', posts)
    return posts


async def main_async():
    # await create_tables()

    async with async_session() as session:
        # await create_user_by_username(session, 'am')
        # await create_author_for_user_by_username(session, "Pam", "Pamela")
        await create_posts_for_user(
            session, "Sam", "Django Lesson", "Python News", "Flask Lesson", "Django Intro"
        )

def main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main_async())


if __name__ == "__main__":
    main()

