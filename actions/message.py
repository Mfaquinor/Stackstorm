import requests
import json
from st2common.runners.base_action import Action

BASE_URL = 'https://harold.indrabrasil.com.br/api-chat/message'


class SlackAction(Action):

    def run(self, **kwargs):
        params = kwargs

        question = params['question']
        channel = params['channel']
        user = params['user']
        bot = params['bot']

        headers = {}
        headers['Content-Type'] = 'application/json'

        self.logger.info(bot)
        self.logger.info(user)
        self.logger.info(channel)
        self.logger.info(question)

        payload = {
            'question': question,
            'user': user
            'botId': bot
            'channelType': channel
        }

        return requests.post(url=BASE_URL, headers=headers, data=json.dumps(payload))