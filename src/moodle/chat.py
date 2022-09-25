import time
from .api import Api
from .models import Message
from requests.exceptions import RequestException
from typing import List, Optional
from pydantic import parse_obj_as


class Chat:
    def __init__(self, credentials: list[str]):
        self._credentials: List[str] = credentials
        self._user_to: Optional[str] = None
        self._last_message: Optional[Message] = None
        self._api = Api(*credentials)

    def connect_chat(self, user_to: str):
        """Start a new chat interface with the user specified"""
        sended = False
        self._user_to = user_to

        print(f"Welcome {self._credentials[1][0].upper()}{self._credentials[1][1:]}, this is the command line moodle "
              f"chat.\nNow you're connect with {self._user_to}, so start to texting!!\nIf you want exit of the chat, "
              "only write \":quit\".\n"
              "Write your message, later press [enter].")

        while not sended:
            message = input("You: ").strip()

            if message == ':quit':
                break
            else:
                sended = self.send(message)

                if not sended:
                    print("Cannot send the message, please try again.")
                else:
                    for resp in parse_obj_as(List[Message], self.wait_response(60 * 15, 15)):
                        print(f"{self._user_to}: {resp.raw_text}")

                    sended = False

    def send(self, message: str) -> bool:
        """Send a message"""
        sended = True
        try:
            resp = self._api.send_message(self._user_to, message.strip())
            if resp:
                self._last_message = resp[-1]
            else:
                sended = False
        except RequestException:
            sended = False

        return sended

    def wait_response(self, waitfor: int, each: int = 15) -> Optional[List[Message]]:
        """Wait for the response of the contact"""
        times = round(waitfor / each)

        while times > 0:
            lasttmsp = (time.time() - 100 * 60 * 60) if not self._last_message else self._last_message.timecreated

            try:
                resp = self._api.get_response(self._user_to, lasttmsp)
                if resp:
                    self._last_message = resp[-1]
                    return resp
            finally:
                times -= 1
                time.sleep(each)

        return None
