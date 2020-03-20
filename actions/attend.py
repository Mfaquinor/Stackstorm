from st2common.runners.base_action import Action

class SlackAction(Action):

    def run(self, **kwargs):
        params = kwargs

        userid = params['userid']
        status = params['status']

        self.logger.info(status)
        self.logger.info(userid)

        key = 'attendance:' + userid

        if(status == 'True' or status == True):
            self.action_service.set_value(name=key, value=status)
        else:
            self.action_service.delete_value(key)


        return True