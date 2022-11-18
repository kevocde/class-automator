from __future__ import annotations
import abc

import psycopg2
import sqlalchemy.exc

from .schemas import BasicUserInfo
from .database import get_db, BasicUserInfoDB

DEFAULT_LIMIT = 10


class Repository(abc.ABC):
    SCHEMA = None
    MODEL = None
    ID_COLUMN = 'id'

    @classmethod
    def find_all(cls, since: int = 0, to: int = DEFAULT_LIMIT) -> list[SCHEMA]:
        pass

    @classmethod
    def find_all_by(cls, filters: list, since: int = 0, to: int = DEFAULT_LIMIT) -> list[SCHEMA]:
        pass

    @classmethod
    def find_by(cls, filters: list) -> SCHEMA:
        pass

    @classmethod
    def create(cls, data: dict) -> SCHEMA:
        db = get_db()
        model = BasicUserInfoDB(**data)
        db.add(model)
        db.commit()
        db.refresh(model)

        return cls.SCHEMA.from_orm(model)

    @classmethod
    def update(cls, identifier, data: dict) -> SCHEMA:
        db = get_db()
        if cls.ID_COLUMN in data:
            del data[cls.ID_COLUMN]

        db.query(cls.MODEL).filter(cls.MODEL.id == identifier).update(values=data)
        db.commit()

        return cls.SCHEMA.from_orm(db.get(cls.MODEL, identifier))

    @classmethod
    def delete(cls, identifier) -> bool:
        pass


class BasicUserInfoRepository(Repository):
    SCHEMA = BasicUserInfo
    MODEL = BasicUserInfoDB

    @classmethod
    def update_or_create(cls, data: dict) -> SCHEMA | None:
        try:
            db = get_db()
            model = db.query(cls.MODEL) \
                .filter(cls.MODEL.user == data['user'] or cls.MODEL.student_code == data['student_code']) \
                .first()

            return cls.create(data) if not model else cls.update(model.id, data)
        except sqlalchemy.exc.DatabaseError:
            return None
