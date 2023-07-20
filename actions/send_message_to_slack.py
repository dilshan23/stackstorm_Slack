import slack
from st2common.runners.base_action import Action

class SendMessageToSlackAction(Action):
    def run(self,text="test"):
        #payload = self.config.get('new_update', {})
        #message = payload["text"]
        client = slack.WebClient(token=self.config['token'])
        m = client.chat_postMessage(text="testing", channel=self.config['channel_id'])
        return m
