from decouple import config
from moodle import Chat


if __name__ == '__main__':
    credentials = [config('ACADEMY_URL'), config('ACADEMY_USERNAME'), config('ACADEMY_PASSWORD')]
    to = 'Sam Student'

    chat = Chat(credentials=credentials)
    chat.connect_chat(to)
