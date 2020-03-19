import requests
import json
from st2common.runners.base_action import Action

BASE_URL = 'https://harold.indrabrasil.com.br/api-chat/message'


class SlackAction(Action):

    def run(self, **kwargs):
        params = kwargs

        username = params['username']
        question = params['question']
        channel = params['channel']
        userid = params['userid']
        bot = params['bot']

        headers = {}
        headers['Content-Type'] = 'application/json'

        self.logger.info(bot)
        self.logger.info(userid)
        self.logger.info(channel)
        self.logger.info(question)
        self.logger.info(username)

        payload = {
            'question': question,
            'user': username,
            'userId': userid,
            'botId': bot,
            'channelType': channel
        }

        return requests.post(url=BASE_URL, headers=headers, data=json.dumps(payload))