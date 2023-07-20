import slack 
from st2reactor.sensor.base import PollingSensor
from st2reactor.sensor.base import Sensor
import eventlet
import re
import time


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
        # while True:
        #     messages = self._client.conversations_history(channel="C01NY5BN06S")
        #     for mes in messages["messages"]:
        #         if mes["text"] not in processed_messages:
        #             text = mes["text"]
        #             pattern = r'mailto(\S+@[^.]+\.[a-zA-Z]+)'
        #             match = re.search(pattern, text)
        #             if match:
        #                 email_address = match.group(1)           
        #                 text1 = "sending email to "+email_address
        #                 payload = {}
        #                 payload["text"] = email_address         
        #                 self.sensor_service.dispatch(trigger="slack_dilshan.new_update", payload=payload,trace_tag="1234")
        #                 self._client.chat_postMessage(text=text1, channel="C01NY5BN06S")
        #                 processed_messages.append(mes["text"])

        #     time.sleep(10)
                    
    def run(self):
        """
        Run infinite loop, continuously reading for Slack Messages,
        dispatch trigger with payload data if message received.
        """
        while not self._stop:
            count = self.sensor_service.get_value("dilshan_slack.count") or 0
            count = count + 1  
            payload = {}
            payload["text"] = "email to "       
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