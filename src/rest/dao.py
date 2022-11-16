from __future__ import annotations

from abc import ABC, abstractmethod
from .database import SessionLocal, engine, Base, BasicUserInfoDB
from .schemas import BasicUserInfo

Base.metadata.create_all(bind=engine)
DEFAULT_LIMIT = 10


def get_db():
    db = SessionLocal()
    try:
        return db
    except:
        db.close()


class Dao(ABC):
    @classmethod
    @abstractmethod
    def get_all(cls, skip: None | int, to: None | int):
        pass

    @abstractmethod
    def find_by_id(self, identifier: int | str):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, identifier: int | str):
        pass

    @abstractmethod
    def delete(self, identifier: int | str) -> bool:
        pass


class BasicUserInfoDao(Dao):
    @classmethod
    def get_all(cls, skip: None | int = None, to: None | int = None) -> list[BasicUserInfo]:
        raw_data = get_db().query(BasicUserInfoDB) \
            .offset(skip if skip else 0) \
            .limit(DEFAULT_LIMIT if not skip else skip) \
            .all()

        return [BasicUserInfo.from_orm(record) for record in raw_data]

    def find_by_id(self, identifier: int | str):
        pass

    def create(cls, data):
        pass

    def update(self, identifier: int | str):
        pass

    def delete(self, identifier: int | str) -> bool:
        pass
