import time

from decouple import config
from moodle_api import MoodlApi


if __name__ == '__main__':
    moodle_api = MoodlApi(
        platform_url=config('ACADEMY_URL'),
        username=config('ACADEMY_USERNAME'),
        password=config('ACADEMY_PASSWORD')
    )

    to = 'Ana Marcela Grijalba Brand'
    message = moodle_api.send_message(to, 'This is a test message')[0]
    response = moodle_api.get_response(to, message['timecreated'])
