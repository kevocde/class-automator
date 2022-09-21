from bs4 import BeautifulSoup
import requests


class MoodlApi:
    def __init__(self, platform_url, username, password):
        self._platform_url = platform_url
        self._username = username
        self._password = password

        self._session = requests.Session()
        self._sesskey = None
        self._last_message_sended = None

    @staticmethod
    def _set_arguments(kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = {}

        kwargs['headers'] |= {'User-Agent': 'PostmanRuntime/7.29.2'}

    def get(self, url, **kwargs):
        url = self._platform_url + url
        self._set_arguments(kwargs)

        return self._session.get(url, **kwargs)

    def post(self, url, *args, **kwargs):
        url = self._platform_url + url
        self._set_arguments(kwargs)

        return self._session.post(url, *args, **kwargs)

    def _login(self):
        # Carga primero el token del formulario
        soup = BeautifulSoup(self.get('/login/index.php').text, 'html.parser')
        logintoken = soup.select_one('input[name="logintoken"]').attrs['value']

        # Solicita el loggeo y obtiene la sesskey
        soup = BeautifulSoup(
            self.post(
                '/login/index.php',
                data={'logintoken': logintoken, 'username': self._username, 'password': self._password}
            ).text,
            'html.parser'
        )
        self._sesskey = soup.select_one('input[name="sesskey"]').attrs['value']

    def send_message(self, conversationid, message):
        methodname = 'core_message_send_messages_to_conversation'
        buffer_messages = []

        if not self._sesskey:
            self._login()

        if isinstance(message, (tuple, list)):
            for text in message:
                buffer_messages.append({'text': text})
        else:
            buffer_messages.append({'text': message})

        self.post(
            f'/lib/ajax/service.php?sesskey={self._sesskey}&info={methodname}',
            json=[{
                'index': 0,
                'methodname': methodname,
                'args': {'conversationid': conversationid, 'messages': buffer_messages}
            }]
        )