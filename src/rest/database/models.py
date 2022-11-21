from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from .database import Base


class BasicUserInfoDB(Base):
    __tablename__ = "basic_user_information"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, unique=True, index=True)
    password = Column(String)
    student_code = Column(String, unique=True, index=True)

    schedules = relationship("ScheduleDB", back_populates="user")


class ScheduleDB(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    lang = Column(String)
    level = Column(String)
    headquarter = Column(String)
    unit_other = Column(String)
    _date = Column("date", Date)
    _time = Column("time", String)
    recurring = Column(Boolean, default=False)
    times = Column(Integer)
    user_id = Column(Integer, ForeignKey("basic_user_information.id"))

    user = relationship("BasicUserInfoDB", back_populates="schedules")
    attemps = relationship("AttemptDB", back_populates="schedule")

    @property
    def time(self):
        return self._time.strip()

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def date(self):
        return self._date.strftime("%Y-%m-%d")

    @date.setter
    def date(self, value):
        self._date = value


class AttemptDB(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    start_execution = Column(TIMESTAMP)
    end_execution = Column(TIMESTAMP, nullable=True)
    message_log = Column(Text, nullable=True)
    successful = Column(Boolean, default=False)
    schedule_id = Column(Integer, ForeignKey("schedules.id"))

    schedule = relationship("ScheduleDB", back_populates="attemps")
