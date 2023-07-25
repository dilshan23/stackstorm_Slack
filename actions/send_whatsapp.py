import requests
from st2common.runners.base_action import Action

class SendWhatsapp(Action):
	# creates SMTP session
	def run(self,receiver_whatsapp_number):

		if receiver_whatsapp_number != "NA":

			# Sample JSON data for the request body
			sample_body = {
			    "whatsapp": receiver_whatsapp_number
			    
			}

			# URL to send the POST request to
			url = "https://ddb8-103-21-165-115.ngrok-free.app"

			# Send the POST request
			response = requests.post(url, json=sample_body)

			# Check the response status code
			if response.status_code == 200:
			    print("Whatsapp message sent ")
			    return "Whatsapp ok"
			else:
			    print(f"Request failed with status code: {response.status_code}")
			    print(response.text)  # Print response content for debugging if needed
			    return "Whatsapp not ok"


		else:
			print("NA for Whatsapp")

		
	            
	    


	   	
	    

	    

	    
	    
	    
	   