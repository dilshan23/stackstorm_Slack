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
#         url = "https://f0a4-112-134-61-244.ngrok-free.app"
#         myobj = {'somekey': 'somevalue'}

#         x = requests.post(url, json = myobj)

#         self._client = slack.WebClient(token=self._config['token'])
#         print(self._client)
#         #self._last_id = None

#     def poll(self):
#         #if not self._last_id:

#         #tetsting if polling workd in 15 second by sendung to my server
#         # url = 'https://c6ef-112-134-57-14.ngrok-free.app'
#         # myobj = {'somekey': 'somevalue'}

#         # x = requests.post(url, json = myobj)


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
        #self.processed_emails = set()


    def setup(self):  # this works
        # Setup stuff goes here. For example, you might establish connections
        # to external system once and reuse it. This is called only once by the system.
        url = 'https://8cc1-112-134-61-244.ngrok-free.app'
        payload = {"text": "email"}
        x = requests.post(url, json = payload)  # this works

        # slack
        self._client = slack.WebClient(token=self._config['token'])
        messages = self._client.conversations_history(channel="C01NY5BN06S")

        #print(messages)
        processed_emails = set()

        import re
        for mes in messages["messages"]:
            print(mes["text"])
            payload = {}
            payload["text"] = mes["text"]
            x = requests.post(url, json = payload)
            text = mes["text"]

            # Define the regex pattern
            pattern = r'bot email to (\S+@[^.]+\.[a-zA-Z]+)'

            # Use re.search to find the match
            match = re.search(pattern, text)

            if match:
                payload1 = {"text":"test"}
                email_address = match.group(1)
            
                text1 = "sending email to "+email_address
                if text1 not in processed_emails:
                    processed_emails.add(text1)

                    #x = requests.post(url, json = payload)
                    self.sensor_service.dispatch(trigger="slack_dilshan.new_update", payload=payload1,trace_tag="1234")
                    self._client.chat_postMessage(text=text1, channel="C01NY5BN06S")
                    

       

    def run(self):
       
        #self._logger.debug("HelloSensor dispatching trigger...")
        count = self.sensor_service.get_value("slack_dilshan.count") or 0
        count = count + 1

        #slack
        messages = self._client.conversations_history(channel="C01NY5BN06S")
        for mes in messages["messages"]:
            print(mes["text"])
            if "email" in mes["text"]:
                payload = {}
                payload["text"] = "test"
                #x = requests.post(url, json = payload)
                self.sensor_service.dispatch(trigger="slack_dilshan.new_update", payload=payload,trace_tag="1234")
                self.sensor_service.set_value("slack_dilshan.count", count)
            
           

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