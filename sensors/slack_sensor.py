from slack import WebClient


class SendMessageToSlackAction():
    def poll(self):
        slack_token = ""
        channel_id = ""

        client = WebClient(token=slack_token)
        messages = client.conversations_history(channel=channel_id)

        if not messages:
            return

        print(messages)

        import time

        current_time = time.time()
        two_minutes_ago = current_time - (2 * 60)  # Convert 2 minutes to seconds

        filtered_messages = []

        for message in messages['messages']:
            timestamp = float(message['ts'])
            if timestamp >= two_minutes_ago and timestamp <= current_time:
                filtered_messages.append(message)

        print(filtered_messages)


bot = SendMessageToSlackAction()
bot.poll()