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

        response = requests.post(url=BASE_URL, headers=headers, data=data)
        results = response.json()

        if not results['ok']:
            failure_reason = ('Failed to perform action %s: %s \(status code: %s)' % (end_point, response.text, response.status_code))
            self.logger.exception(failure_reason)
            raise Exception(failure_reason)

        return results