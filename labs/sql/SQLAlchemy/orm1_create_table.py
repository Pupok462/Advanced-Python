from sqlalchemy import (
    create_engine,
    Float,
    Column,
    Integer,
    String,
    DateTime,
)
from datetime import datetime

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
)

DB_URL = "postgresql+pg8000://user:1234@localhost:5432/blog"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=engine, cls=Base)


class Workers(Base):
    __tablename__ = "workers"
    worker = Column(String(20), unique=True)
    function = Column(String, unique=False)
    salary = Column(Float)
    priority = Column(Integer)
    add_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return (
            f" {self.id} |"
            f" {self.worker!r} |"
            f" {self.function} |"
            f"    {self.priority}      |"
            f" {self.salary} |"
            f" {self.add_at} \n"

        )

    def __repr__(self):
        return str(self)

    def promote(self):
        self.priority += 1


def create_table():
    """ SQL_CODE -->
    CREATE TABLE workers (
        id SERIAL NOT NULL,
        worker VARCHAR(20),
        function VARCHAR,
        salary FLOAT,
        priority INTEGER,
        add_at TIMESTAMP WITHOUT TIME ZONE,
        PRIMARY KEY (id),
        UNIQUE (worker)
    )
    """
    Base.metadata.create_all()


def drop_table():
    """
    SQL_CODE
    DROP TABLE workers
    """
    Base.metadata.drop_all()


def add_worker_to_table(session: SessionType, worker: str, function: str, salary: float, priority: int) -> Workers:
    worker = Workers(worker=worker, function=function, salary=salary, priority=priority)
    print(f"worker {worker} add to Table")

    session.add(worker)
    session.commit()

    print(f"worker {worker} saved in the Table")
    return worker


def show_all_workers(session: SessionType) -> list[Workers]:
    workers = session.query(Workers).all()
    print(f"Received Workers: \n  ID   WORKER   FUNCTION    PRIORITY  SALARY    ADD AT \n {workers}")

    return workers


def find_worker_by_name(session: SessionType, worker: str) -> Workers:
    worker = session.query(Workers).filter_by(worker=worker).one_or_none()
    # worker = session.query(worker).filter_by(worker=worker).first()
    # worker = session.query(worker).filter_by(worker=worker).one()
    print(f"founded worker -> {worker}")
    return worker


def find_workers_by_function(session: SessionType, function: str) -> list[Workers]:
    workers = session.query(Workers).filter_by(function=function)
    all_workers = workers.all()
    print(f"founded workers -> \n {all_workers}")
    return workers


def sort_workers_by_salary(session: SessionType) -> list[Workers]:
    """
    SQL_CODE
    SELECT workers.id AS workers_id,
        workers.worker AS workers_worker,
        workers.function AS workers_function,
        workers.salary AS workers_salary,
        workers.priority AS workers_priority,
        workers.add_at AS workers_add_at
    FROM workers
    ORDER BY workers.salary
    """
    sorted_workers = session.query(Workers).order_by(Workers.salary).all()
    print('Sorted table ->\n', sorted_workers)
    return sorted_workers


def change_priority(session: SessionType, worker: Workers) -> Workers:
    print(f"Worker before -> {worker}")
    worker.promote()
    session.commit()
    print(f"after commit -> {worker}")
    return worker


def find_workers_by_name(session: SessionType, name_part: str) -> list[Workers]:
    """
    SELECT * FROM workers
    WHERE workers.worker LIKE %s
    """
    q_worker = session.query(Workers)

    q_workers_match = q_worker.filter(
        Workers.worker.like(f"%{name_part}")
    ).all()

    print(f"found workers for {name_part!r} \n", q_workers_match)
    return q_workers_match


def delete_worker_by_name(session: SessionType, worker: str) -> Workers:
    """
    SQL_CODE
     DELETE FROM workers WHERE workers.id = %s
    """
    founded_worker = find_worker_by_name(session, worker)
    session.delete(founded_worker)
    session.commit()
    print(f"worker {worker} removed from the Table")
    return founded_worker


def main():
    session: SessionType = Session()
    # add_worker_to_table(session, function="Doctor", salary=200, priority=1, worker="Bob")
    # show_all_workers(session)
    # worker_david = find_worker_by_name(session, worker="David")
    # find_workers_by_function(session, "Manager")
    # change_priority(session, worker_david)
    # delete_worker_by_name(session, "Vova")
    # sort_workers_by_salary(session)
    find_workers_by_name(session, "am")


if __name__ == "__main__":
    main()
