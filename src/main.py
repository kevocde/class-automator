from decouple import config
from moodle_api import MoodlApi


if __name__ == '__main__':
    moodle_api = MoodlApi(
        platform_url=config('ACADEMY_URL'),
        username=config('ACADEMY_USERNAME'),
        password=config('ACADEMY_PASSWORD')
    )

    moodle_api.send_message(2339, "Hi Ana, I'm a robot")
