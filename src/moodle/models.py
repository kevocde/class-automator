from typing import List, Optional
from pydantic import BaseModel
from bs4 import BeautifulSoup


class Message(BaseModel):
    id: Optional[int]
    text: str
    timecreated: Optional[int]
    useridfrom: Optional[int]

    @property
    def raw_text(self) -> str:
        return BeautifulSoup(self.text, 'html.parser').getText()


class Member(BaseModel):
    id: int
    fullname: str


class Conversation(BaseModel):
    id: int
    members: List[Member]
    messages: List[Message]
