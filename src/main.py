from decouple import config
from bs4 import BeautifulSoup
import requests


class RequestMaker:
    def __init__(self, url):
        self._url = url
        self._session = requests.Session()
        self._headers = {'User-Agent': 'PostmanRuntime/7.29.2'}

    def set_arguments(self, kwargs):
        """Merge the default arguments with the arguments passed"""
        kwargs['headers'] = self._headers | (kwargs['headers'] if 'headers' in kwargs else {})

    def get(self, url, **kwargs):
        self.set_arguments(kwargs)
        return self._session.get(self._url + url, **kwargs)

    def post(self, url, *args, **kwargs):
        self.set_arguments(kwargs)
        return self._session.post(self._url + url, *args, **kwargs)


if __name__ == '__main__':
    request = RequestMaker(config('ACADEMY_URL'))

    # Load the login page to get logintoken and the cookie
    response = request.get('/login/index.php')
    soup = BeautifulSoup(response.text, 'html.parser')
    logintoken = soup.select_one('input[name="logintoken"]').attrs['value']

    # Send the login request
    response = request.post(
        '/login/index.php',
        data={'logintoken': logintoken, 'username': config('ACADEMY_USERNAME'), 'password': config('ACADEMY_PASSWORD')}
    )
    soup = BeautifulSoup(response.text, 'html.parser')
    sesskey = soup.select_one('input[name="sesskey"]').attrs['value']

    # Send Message
    data = [
        {
            'index': 0,
            'methodname': 'core_message_send_messages_to_conversation',
            'args': {
                'conversationid': 2115,
                'messages': [{'text': 'Lorem ipsum sdfadfsfsdf programar clase de ingles para tal dia'}]
            }
        }
    ]
    response = request.post(
        f'/lib/ajax/service.php?sesskey={sesskey}&info=core_message_send_messages_to_conversation',
        json=data)

    print(response.text)
