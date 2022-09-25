import time
from moodle_api import MoodleApi


class Chat:
    def __init__(self, credentials: list[str]):
        self._credentials = credentials
        self._user_to = None
        self._last_message = []
        self._moodleapi = MoodleApi(*credentials)

    def connect_chat(self, user_to: str):
        sended = False
        self._user_to = user_to

        print(f"Welcome {self._credentials[-2]}, this is the command line moodle chat.\n"
              f"Now you're connect with {self._user_to}, so start to texting!!\n"
              "If you want exit of the chat, only write \":quit\".\n"
              "Write your message, later press enter.")

        while not sended:
            message = input("You: ").strip()

            if message == ':quit':
                break
            else:
                sended = self.send(message)

                if not sended:
                    print("Cannot send the message, please try again.")
                else:
                    for resp in self.wait_response(60 * 15, 15):
                        print(f"{self._user_to}: {resp['text']}")

                    sended = False

    def send(self, message: str):
        try:
            self._last_message = self._moodleapi.send_message(self._user_to, message)[-1]
            return True
        except Exception as ex:
            print(ex)
            return False

    def wait_response(self, waitfor: int, each: int = 60):
        times = round(waitfor / each)

        while times > 0:
            lasttmsp = (time.time() - 100 * 60 * 60) if not self._last_message else self._last_message['timecreated']

            try:
                resp = self._moodleapi.get_response(self._user_to, lasttmsp)
                if len(resp) > 0:
                    self._last_message = resp[-1]
                    return resp
            except Exception:
                pass
            finally:
                times -= 1
                time.sleep(each)

        return []