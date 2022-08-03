"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from models import session_factory, Base, engine, AsyncSession, User, Post
import sys
import asyncio
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def insert_users_posts_in_db(session: AsyncSession):
    users_data, post_data = await asyncio.gather(
        fetch_json(USERS_DATA_URL), fetch_json(POSTS_DATA_URL)
    )

    users = []
    for user_data in users_data:
        user = User(
            name=user_data.get("name"),
            username=user_data.get("username"),
            email=user_data.get("email"),
            id=user_data.get("id"),
        )
        users.append(user)
    session.add_all(users)

    for post in post_data:
        session.add(
            Post(
                user_id=post.get("userId"),
                title=post.get("title"),
                body=post.get("body"),
                id=post.get("id"),
            )
        )

    await session.commit()


async def async_main():
    # await create_tables()
    async with session_factory() as session:
        await insert_users_posts_in_db(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
