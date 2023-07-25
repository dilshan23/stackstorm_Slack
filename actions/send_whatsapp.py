import requests
from st2common.runners.base_action import Action

class SendWhatsapp(Action):
	# creates SMTP session
	def run(self,receiver_whatsapp_number):

		# Sample JSON data for the request body
		sample_body = {
		    "whatsapp": receiver_whatsapp_number
		    
		}

		# URL to send the POST request to
		url = "https://3a6f-175-157-233-97.ngrok-free.app"

		# Send the POST request
		response = requests.post(url, json=sample_body)

		# Check the response status code
		if response.status_code == 200:
		    print("Whatsapp message sent ")
		else:
		    print(f"Request failed with status code: {response.status_code}")
		    print(response.text)  # Print response content for debugging if needed

		
	            
	    


	   	
	    

	    

	    
	    
	    
	   