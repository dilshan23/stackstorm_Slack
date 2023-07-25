from st2common.runners.base_action import Action
import requests


class SendSms(Action):
	# creates SMTP session
	def run(self,receiver_sms):

		if receiver_sms != "NA":
		

			# Sample JSON data for the request body
			sample_body = {
			    "sms": receiver_sms
			    
			}

			# URL to send the POST request to
			url = "https://ddb8-103-21-165-115.ngrok-free.app"

			# Send the POST request
			response = requests.post(url, json=sample_body)

			# Check the response status code
			if response.status_code == 200:
			    print("Request sent ")
			    return "SMS ok"
			else:
			    print(f"Request failed with status code: {response.status_code}")
			    print(response.text)  # Print response content for debugging if needed
			    return "SMS not ok"

		else:
			print("SMS NA")


			