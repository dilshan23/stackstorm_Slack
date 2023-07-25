from st2common.runners.base_action import Action
import requests


class SendSms(Action):
	# creates SMTP session
	def run(self,receiver_sms):
		

		# Sample JSON data for the request body
		sample_body = {
		    "sms": receiver_sms
		    
		}

		# URL to send the POST request to
		url = "https://3a6f-175-157-233-97.ngrok-free.app"

		# Send the POST request
		response = requests.post(url, json=sample_body)

		# Check the response status code
		if response.status_code == 200:
		    print("Request sent ")
		else:
		    print(f"Request failed with status code: {response.status_code}")
		    print(response.text)  # Print response content for debugging if needed


			