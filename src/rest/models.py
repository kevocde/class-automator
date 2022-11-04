from pydantic import BaseModel
from enum import Enum


class AvailableLanguages(str, Enum):
    english: str = "en"
    french: str = "fr"


class BasicUserInfo(BaseModel):
    platform: str
    user: str
    password: str

    def to_credentials(self):
        """Get list with information of credentials"""
        return [self.platform, self.user, self.password]


class ClassDetails(BaseModel):
    lang: AvailableLanguages
    level: str
    headquarter: str
    studentCode: str
    unitOther: str
