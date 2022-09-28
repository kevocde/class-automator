from decouple import config
from src.moodle import Chat


if __name__ == '__main__':
    credentials = [config('ACADEMY_URL'), config('ACADEMY_USERNAME'), config('ACADEMY_PASSWORD')]
    to = 'English Teacher - Professeur de Français'

    chat = Chat(credentials=credentials)
    chat.connect_chat(to)
