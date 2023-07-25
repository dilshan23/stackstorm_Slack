import slack
from st2common.runners.base_action import Action

class SendMessageToSlackAction(Action):
    def run(self,text="test",whatsapp_output="ok"):
        if text is not None:
            text = "sent email to " + text
        else:
            text = "email is None"  # Or some default message if text is None
        text = text+whatsapp_status
        client = slack.WebClient(token=self.config['token'])
        m = client.chat_postMessage(text=text, channel=self.config['channel_id'])
        return m
