import requests
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

        data = {}
        data['channelType'] = channel
        data['question'] = question
        data['botId'] = bot
        data['user'] = user

        return requests.post(url=BASE_URL, headers=headers, data=data)