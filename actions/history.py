import requests
import json
from st2common.runners.base_action import Action

BASE_URL = 'https://harold.indrabrasil.com.br/api-chat/message/history'


class SlackAction(Action):

    def run(self, **kwargs):
        params = kwargs

        userid = params['userid']
        bot = params['bot']

        headers = {}
        headers['Content-Type'] = 'application/json'

        self.logger.info(bot)
        self.logger.info(userid)

        payload = {
            'clientId': userid,
            'botId': bot,
        }

        response = requests.post(url=BASE_URL, headers=headers, data=json.dumps(payload))

        return response.json()