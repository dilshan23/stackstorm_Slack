import slack 
from st2reactor.sensor.base import PollingSensor

class SlackSensor(PollingSensor):

    def __init__(self, sensor_service, config, poll_interval):
        super(SlackSensor, self).__init__(sensor_service=sensor_service,
                                             config=config,
                                             poll_interval=poll_interval)
        self._trigger_name = 'new_update'
        self._trigger_pack = 'slack_dilshan'
        self._trigger_ref = '.'.join([self._trigger_pack, self._trigger_name])

    def setup(self):
        self._client = slack.WebClient(token=self._config['token'])
        #self._last_id = None

    def poll(self):
        #if not self._last_id:
        updates = self._client.conversations_history(channel=self._config['channel_id'])
        #else:
        #updates = self._client.getUpdates(offset=self._last_id + 1)

        if updates:
            for u in updates:
                self._dispatch_trigger(u.to_dict())
            #self._last_id = updates[-1].update_id

    def update_trigger(self):
        pass

    def add_trigger(self, trigger):
        pass

    def cleanup(self):
        pass

    def remove_trigger(self):
        pass

    def _dispatch_trigger(self, update):
        trigger = self._trigger_ref
        self._sensor_service.dispatch(trigger, update)

    # def poll(self):
    #     slack_token = ""
    #     channel_id = ""

    #     client = WebClient(token=slack_token)
    #     messages = client.conversations_history(channel=channel_id)

    #     if not messages:
    #         return

    #     print(messages)

    #     import time

    #     current_time = time.time()
    #     two_minutes_ago = current_time - (2 * 60)  # Convert 2 minutes to seconds

    #     filtered_messages = []

    #     for message in messages['messages']:
    #         timestamp = float(message['ts'])
    #         if timestamp >= two_minutes_ago and timestamp <= current_time:
    #             filtered_messages.append(message)

    #     print(filtered_messages)


if __name__ == '__main__':
    
    bot = SendMessageToSlackAction()
    bot.poll()