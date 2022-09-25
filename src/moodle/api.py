from bs4 import BeautifulSoup
import requests


class Api:
    def __init__(self, platform_url, username, password):
        self._platform_url = platform_url
        self._username = username
        self._password = password

        self._session = requests.Session()
        self._sesskey = None
        self._userid = None
        self._last_message_sended = None

    @staticmethod
    def _set_arguments(kwargs):
        """Adds to the parameters, defaults values, for example the header \"User-Agent\""""
        if 'headers' not in kwargs:
            kwargs['headers'] = {}

        kwargs['headers'] |= {'User-Agent': 'PostmanRuntime/7.29.2'}

    def get(self, url, **kwargs):
        """Sends a get request"""
        url = self._platform_url + url
        self._set_arguments(kwargs)

        return self._session.get(url, **kwargs)

    def post(self, url, *args, **kwargs):
        """Sends a post request"""
        url = self._platform_url + url
        self._set_arguments(kwargs)

        return self._session.post(url, *args, **kwargs)

    def _consume_service(self, methodname, method='get', *args, **kwargs):
        """Consumes a determinate service with the prefix service.php"""
        url = f'/lib/ajax/service.php?sesskey={self._sesskey}&info={methodname}'
        if method == 'get':
            return self.get(url, **kwargs)
        elif method == 'post':
            return self.post(url, *args, **kwargs)
        else:
            raise ReferenceError

    def _login(self):
        """Login on the site"""
        # First load the token
        soup = BeautifulSoup(self.get('/login/index.php').text, 'html.parser')
        logintoken = soup.select_one('input[name="logintoken"]').attrs['value']

        # Later sends the login information form
        resp = self.post(
            '/login/index.php',
            data={'logintoken': logintoken, 'username': self._username, 'password': self._password}
        )

        # At the last, load the dashboard and get the sesskey and the userid
        if resp.status_code < 400:
            soup = BeautifulSoup(self.get('/my').text, 'html.parser')
            self._sesskey = soup.select_one('input[name="sesskey"]').attrs['value']
            self._userid = soup.select_one('[data-userid]').attrs['data-userid']
        else:
            raise Exception("Cannot login in the site")

    def send_message(self, to, messages):
        """Sends a message to determinate user"""
        methodname = 'core_message_send_messages_to_conversation'
        conversation = self.get_conversation_by_member_name(to)

        if conversation:
            if isinstance(messages, (tuple, list)):
                messages = [{'text': message} for message in messages]
            else:
                messages = [{'text': messages}]

            response = self._consume_service(
                methodname,
                method='post',
                json=[{
                    'index': 0,
                    'methodname': methodname,
                    'args': {'conversationid': conversation['id'], 'messages': messages}
                }]
            )

            return response.json()[0]['data']
        else:
            return []

    def get_conversation_by_member_name(self, name):
        """Look for the conversation information by the name of the user"""
        methodname = 'core_message_get_conversations'

        if not self._sesskey:
            self._login()

        response = self._consume_service(
            methodname,
            method='post',
            json=[{
                'index': 0,
                'methodname': methodname,
                'args': {
                    'userid': self._userid,
                    'type': 1,
                    'limitnum': 51,
                    'limitfrom': 0,
                    'favourites': False,
                    'mergeself': True,
                }
            }]
        )

        if response.status_code == 200:
            response = response.json()

            if len(response) \
                    and 'data' in response[0] \
                    and 'conversations' in response[0]['data']:
                for conv in response[0]['data']['conversations']:
                    for member in conv['members']:
                        if member['fullname'] == name:
                            return conv

        return None

    def get_response(self, fromu, last_timestamp):
        """Consumes the service to get the response of the userfrom and later return one"""
        methodname = 'core_message_get_conversation_messages'
        messages = []
        conversation = self.get_conversation_by_member_name(fromu)

        if conversation:
            response = self._consume_service(
                methodname,
                method='post',
                json=[{
                    'index': 0,
                    'methodname': methodname,
                    'args': {
                        'currentuserid': self._userid,
                        'convid': conversation['id'],
                        'newest': True,
                        'limitnum': 0,
                        'limitfrom': 0,
                        'timefrom': last_timestamp
                    }
                }]
            )

            if response.status_code == 200:
                response = response.json()

                if len(response) \
                        and 'data' in response[0] \
                        and 'messages' in response[0]['data']:
                    for message in response[0]['data']['messages']:
                        if message['timecreated'] >= last_timestamp and int(message['useridfrom']) != int(self._userid):
                            message['text'] = BeautifulSoup(message['text'], 'html.parser').getText()
                            messages.append(message)

        return messages
