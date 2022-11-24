from __future__ import annotations
import abc
from datetime import datetime, timedelta

from sqlalchemy import exc, select, func

from .schemas import BasicUserInfo, Schedule
from .database import get_db, BasicUserInfoDB, ScheduleDB, AttemptDB

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
    def create(cls, data: dict) -> (int, SCHEMA):
        db = get_db()
        model = cls.MODEL(**data)
        db.add(model)
        db.commit()
        db.refresh(model)

        return model.id, cls.SCHEMA.from_orm(model)

    @classmethod
    def update(cls, identifier, data: dict) -> (int, SCHEMA):
        db = get_db()
        if cls.ID_COLUMN in data:
            del data[cls.ID_COLUMN]

        db.query(cls.MODEL).filter(cls.MODEL.id == identifier).update(values=data)
        db.commit()

        return identifier, cls.SCHEMA.from_orm(db.get(cls.MODEL, identifier))

    @classmethod
    def delete(cls, identifier) -> bool:
        pass


class BasicUserInfoRepository(Repository):
    SCHEMA = BasicUserInfo
    MODEL = BasicUserInfoDB

    @classmethod
    def update_or_create(cls, data: dict) -> (int, SCHEMA) | None:
        try:
            db = get_db()
            model = db.query(cls.MODEL) \
                .filter(cls.MODEL.user == data['user'] or cls.MODEL.student_code == data['student_code']) \
                .first()

            return cls.create(data) if not model else cls.update(model.id, data)
        except exc.DatabaseError:
            return None


class SchedulesRepository(Repository):
    SCHEMA = Schedule
    MODEL = ScheduleDB

    @classmethod
    def find_next_shedules_to_schedule(cls) -> list[tuple[int, SCHEMA]] | None:
        try:
            current = datetime.now() + timedelta(hours=12, days=2)
            db = get_db()

            attempts_query = (
                select(func.count(AttemptDB.id))
                .where(ScheduleDB.id == AttemptDB.schedule_id and AttemptDB.successful)
                .scalar_subquery()
            )

            result = db.query(ScheduleDB)\
                .where(
                    ScheduleDB.__dict__['_date'] == current.date()
                    and ScheduleDB.times < attempts_query.scalar_subquery()
                )\
                .all()

            return [(row.id, Schedule.from_orm(row)) for row in result]
        except Exception as err:
            print(err)
            return None
