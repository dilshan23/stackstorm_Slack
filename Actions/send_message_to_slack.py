from slack import WebClient

#from st2common.runners.base_action import Action

#https://gist.github.com/demmer/617afb2575c445ba25afc432eb37583b

class SendMessageToSlackAction():
    def run(self, message):
        slack_token = ""
        channel_id = ""

        client = WebClient(token=slack_token)
        response = client.chat_postMessage(channel=channel_id, text=message)

        if response["ok"]:
            return True
        else:
            return False


        

        # last_message_timestamp = self._handle_result(result=result)

        # if last_message_timestamp:
        #     self._set_last_message_timestamp(
        #         last_message_timestamp=last_message_timestamp)

    def _handle_result(self, result):
        """
        Handle / process the result and return timestamp of the last message.
        """
        existing_last_message_timestamp = self._get_last_message_timestamp()
        new_last_message_timestamp = existing_last_message_timestamp

        for item in result:
            item_type = item['type']
            item_timestamp = int(float(item.get('ts', 0)))

            if (existing_last_message_timestamp and
                    item_timestamp <= existing_last_message_timestamp):
                # We have already seen this message, skip it
                continue

            if item_timestamp > new_last_message_timestamp:
                new_last_message_timestamp = item_timestamp

            handler_func = self._handlers.get(item_type, lambda data: data)
            handler_func(data=item)

        return new_last_message_timestamp

    # def _set_last_message_timestamp(self, last_message_timestamp):
    #     self._last_message_timestamp = last_message_timestamp
    #     name = self.DATASTORE_KEY_NAME
    #     value = str(last_message_timestamp)
    #     self._sensor_service.set_value(name=name, value=value)
    #     return last_message_timestamp


bot = SendMessageToSlackAction()
bot.run("hi")
