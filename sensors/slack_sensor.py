import slack 
from st2reactor.sensor.base import PollingSensor
from st2reactor.sensor.base import Sensor
import eventlet
import re
import time


#processed_messages = []  # important ... this needs to move to caching

class SlackSensor(Sensor):
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
        super(SlackSensor, self).__init__(sensor_service=sensor_service, config=config)
        self._logger = self._sensor_service.get_logger(__name__)
        self._stop = False


    def setup(self): 
        # Setup stuff goes here. For example, you might establish connections
        # to external system once and reuse it. This is called only once by the system.

        self._client = slack.WebClient(token=self._config['token'])
        self.messages = self._client.conversations_history(channel="C01NY5BN06S")
        
        processed_messages = []  # important ... this needs to move to caching
        while True:
            messages = self._client.conversations_history(channel="C01NY5BN06S")
            for mes in messages["messages"]:
                if mes["text"] not in processed_messages:
                    text = mes["text"]
                    pattern = r'mailto(\S+@[^.]+\.[a-zA-Z]+)'
                    match = re.search(pattern, text)
                    if match:
                        email_address = match.group(1)           
                        payload = {}  
                        payload["receiver_email"] = email_address.split('|')[0] 

                        #whatssapp
                        whatsapp_pattern = r'whatsapp:"([^"]*)"'
                        match1 = re.search(whatsapp_pattern, text)
                        if match1:
                            payload["receiver_whatsapp_number"] = match1.group(1)

                        #sms
                        sms_pattern = r'sms:"([^"]*)"'
                        match2 = re.search(sms_pattern, text)
                        if match1:
                            payload["receiver_sms"] = match2.group(1)


                        self.sensor_service.dispatch(trigger="slack_dilshan.new_update", payload=payload,trace_tag="1234")
                        processed_messages.append(mes["text"])

            time.sleep(10)
                    
    def run(self):
        """
        Run infinite loop, continuously reading for Slack Messages,
        dispatch trigger with payload data if message received.
        """
        while not self._stop:
            count = self.sensor_service.get_value("dilshan_slack.count") or 0
            count = count + 1  
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


# class SlackPollSensor(PollingSensor): 

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
       
#         updates = self._client.conversations_history(channel="C01NY5BN06S")
#         paylaod= {} #make a payload to a trigger (python dict)
#         updates = {"text":"test"}
#         if updates:  #we got a message
#             self._logger.debug("HelloSensor dispatching trigger...")
            
#             payload["text"] = "email"  #testing with hardcodeed

#             #dispacth to trigger
#             self._dispatch_trigger(payload)
        

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