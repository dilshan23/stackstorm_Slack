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
        print(self._client)
        #self._last_id = None

    def poll(self):
        #if not self._last_id:
        updates = self._client.conversations_history(channel=self._config['channel_id'])
        paylaod= {} #make a payload to a trigger (python dict)
        if updates:  #we got a message
            
            payload["text"] = "test"  #testing with hardcodeed

            #dispacth to trigger
            self._dispatch_trigger(payload)
        #else:
        #updates = self._client.getUpdates(offset=self._last_id + 1)

        # if updates:
        #     for u in updates:
        #         self._dispatch_trigger(u.to_dict())
            #self._last_id = updates[-1].update_id

    def update_trigger(self):
        pass

    def add_trigger(self, trigger):
        pass

    def cleanup(self):
        pass

    def remove_trigger(self):
        pass

    # def _dispatch_trigger(self, update):
    #     trigger = self._trigger_ref
    #     self._sensor_service.dispatch(trigger, update)
    #     print("Trigger dispatched:", trigger, "with update:", update)

    def _dispatch_trigger(self, payload):
        trigger = self._trigger_ref
        self._sensor_service.dispatch(trigger, payload)

