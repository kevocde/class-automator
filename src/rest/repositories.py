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
    def find_next_shedules_to_schedule(cls) -> list[tuple[int, SCHEMA, int]] | None:
        try:
            current = datetime.now() + timedelta(hours=12, days=2)
            db = get_db()

            attempts_query = (
                select(func.count(AttemptDB.id))
                .where(ScheduleDB.id == AttemptDB.schedule_id)
                .scalar_subquery()
            )

            result = db.query(ScheduleDB, attempts_query)\
                .where(
                    ScheduleDB.__dict__['_date'] == current.date()
                    and ScheduleDB.id == AttemptDB.schedule_id
                )\
                .all()

            return [
                (
                    row[0].id,
                    Schedule(
                        **{
                            'date': row[0].date,
                            'time': row[0].time,
                            'recurring': row[0].recurring,
                            'times': row[0].times,
                            'user': row[0].user,
                            'class_details': {
                                'lang': row[0].lang.strip(),
                                'level': row[0].level.strip(),
                                'headquarter': row[0].headquarter,
                                'student_code': row[0].user.student_code,
                                'unit_other': row[0].unit_other
                            }
                        }
                    ),
                    row[1]
                )
                for row in result
            ]
        except Exception as err:
            print(err)
            return None
