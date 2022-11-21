from pydantic import BaseModel as Base
from enum import Enum


class BaseModel(Base):
    @classmethod
    def from_orm_list(cls, data: list) -> list:
        return [cls.from_orm(record) for record in data]


class AvailableLanguages(str, Enum):
    english: str = "en"
    french: str = "fr"


class AvailableTimes(str, Enum):
    sixToEigth: str = "6-8"
    eigthToTen: str = "8-10"
    tenToTwelve: str = "10-12"
    oneToTree: str = "1-3"
    treeToFive: str = "3-5"
    fiveToSeven: str = "5-7"
    sevenToNine: str = "7-9"


class AvailableLevels(str, Enum):
    a1: str = "A1"
    a2: str = "A2"
    b1: str = "B1"
    b1more: str = "B1+"
    b2: str = "B2"
    c1: str = "C1"
    c2: str = "C2"


class BasicUserInfo(BaseModel):
    platform: str | None
    user: str
    password: str

    def to_credentials(self):
        """Get list with information of credentials"""
        return [self.platform, self.user, self.password]

    class Config:
        orm_mode = True


class ClassDetails(BaseModel):
    lang: AvailableLanguages
    level: str
    headquarter: str
    student_code: str
    unit_other: str

    class Config:
        orm_mode = True


class Schedule(BaseModel):
    date: str
    time: AvailableTimes
    recurring: bool
    times: int

    class Config:
        orm_mode = True
