import slack 
from st2reactor.sensor.base import PollingSensor
import requests
import time

import eventlet

# class SlackSensor(PollingSensor):

#     def __init__(self, sensor_service, config, poll_interval):
#         super(SlackSensor, self).__init__(sensor_service=sensor_service,
#                                              config=config,
#                                              poll_interval=poll_interval)
#         self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
#         self._trigger_name = 'new_update'
#         self._trigger_pack = 'slack_dilshan'
#         self._trigger_ref = '.'.join([self._trigger_pack, self._trigger_name])

#     def setup(self):
#         self._client = slack.WebClient(token=self._config['token'])
#         print(self._client)
#         #self._last_id = None

#     def poll(self):
#         #if not self._last_id:

#         #tetsting if polling workd in 15 second by sendung to my server
#         url = 'https://c6ef-112-134-57-14.ngrok-free.app'
#         myobj = {'somekey': 'somevalue'}

#         x = requests.post(url, json = myobj)


#         updates = self._client.conversations_history(channel=self._config['channel_id'])
#         paylaod= {} #make a payload to a trigger (python dict)
#         updats = {"text":"test"}
#         if updates:  #we got a message
#             self._logger.debug("HelloSensor dispatching trigger...")
            
#             payload["text"] = "test"  #testing with hardcodeed

#             #dispacth to trigger
#             self._dispatch_trigger(payload)
#         #else:
#         #updates = self._client.getUpdates(offset=self._last_id + 1)

#         # if updates:
#         #     for u in updates:
#         #         self._dispatch_trigger(u.to_dict())
#             #self._last_id = updates[-1].update_id

#     def update_trigger(self):
#         pass

#     def add_trigger(self, trigger):
#         pass

#     def cleanup(self):
#         pass

#     def remove_trigger(self):
#         pass

#     # def _dispatch_trigger(self, update):
#     #     trigger = self._trigger_ref
#     #     self._sensor_service.dispatch(trigger, update)
#     #     print("Trigger dispatched:", trigger, "with update:", update)

#     def _dispatch_trigger(self, payload):
#         trigger = self._trigger_ref
#         self._sensor_service.dispatch(trigger, payload)

from st2reactor.sensor.base import Sensor


class SampleSensor(Sensor):
    """
    * self.sensor_service
        - provides utilities like
            - get_logger() - returns logger instance specific to this sensor.
            - dispatch() for dispatching triggers into the system.
    * self._config
        - contains parsed configuration that was specified as
          config.yaml in the pack.
    """

    def __init__(self, sensor_service, config):
        super(SampleSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self.sensor_service.get_logger(name=self.__class__.__name__)
        self._stop = False

    def setup(self):
        # Setup stuff goes here. For example, you might establish connections
        # to external system once and reuse it. This is called only once by the system.
        url = 'https://c6ef-112-134-57-14.ngrok-free.app'
        payload = {"text": "email"}
        x = requests.post(url, json = payload)
        #pass

    def run(self):
        url = 'https://c6ef-112-134-57-14.ngrok-free.app'
        payload = {"text": "email"}

        while not self._stop:
            #self._logger.debug("HelloSensor dispatching trigger...")
            count = self.sensor_service.get_value("dilshan_slack.count") or 0
            count = count + 1
            #x = requests.post(url, json = payload)
            self.sensor_service.dispatch(trigger="dilshan_slack.new_update", payload=payload,trace_tag="1234")
            self.sensor_service.set_value("dilshan_slack.count", count)
            eventlet.sleep(10)
           

    def cleanup(self):
        # This is called when the st2 system goes down. You can perform cleanup operations like
        # closing the connections to external system here.
        pass

    def add_trigger(self, trigger):
        # This method is called when trigger is created
        pass

    def update_trigger(self, trigger):
        # This method is called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # This method is called when trigger is deleted
        pass