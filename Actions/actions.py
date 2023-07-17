from slack import WebClient
from st2common.runners.base_action import Action

class SendMessageToSlackAction(Action):
    def run(self, message):
        slack_token = "YOUR_SLACK_TOKEN"
        channel_id = "YOUR_CHANNEL_ID"

        client = WebClient(token=slack_token)
        response = client.chat_postMessage(channel=channel_id, text=message)

        if response["ok"]:
            return True
        else:
            return False
