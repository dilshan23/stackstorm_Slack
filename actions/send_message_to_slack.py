import slack
from st2common.runners.base_action import Action

class SendMessageToSlackAction(Action):
    def run(self,text="test"):
        if text is not None:
            text = "sent email to " + text
        else:
            text = "email is None"  # Or some default message if text is None
        client = slack.WebClient(token=self.config['token'])
        m = client.chat_postMessage(text=text, channel=self.config['channel_id'])
        return m
