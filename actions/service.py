import requests
import json

from st2common.runners.base_action import Action

HAROLD = 'https://localhost/api/v1/webhooks/harold/message'
CONNECTACHAT = 'https://localhost/api/v1/webhooks/oop/message'

BASE_URL = ''

AUTH='?st2-api-key='

class SlackAction(Action):

    def run(self, **kwargs):
        params = kwargs

        username = params['username']
        message = params['message']
        userid = params['userid']
        token = params['token']

        key = 'attendance:' + userid
        attendance = self.action_service.get_value(key)

        self.logger.info(attendance)

        if(attendance is None):
            BASE_URL = HAROLD
        else:
            BASE_URL = CONNECTACHAT


        headers = {}
        headers['Content-Type'] = 'application/json'

        payload = {
            'message': message,
            'username': username,
            'userid': userid
        }

        return requests.post(url=BASE_URL + AUTH + token, headers=headers, data=json.dumps(payload), verify=False)