import slack
from st2common.runners.base_action import Action

class SendMessageToSlackAction(Action):
    def run(self,text="test"):
        client = slack.WebClient(token=self.config['token'])
        m = client.chat_postMessage(text="sent email to" +text, channel=self.config['channel_id'])
        return m
