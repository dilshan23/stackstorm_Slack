import smtplib
from st2common.runners.base_action import Action
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

class SendMessageToSlackAction(Action):
	# creates SMTP session
	# def run(self,receiver_email):

	# 	sender_email=self.config['sender_email']
	# 	sender_password = self.config['sender_password']
	# 	subject = self.config['subject']
	# 	body = self.config['body']
	# 	msg = MIMEMultipart()
	# 	msg['From'] = sender_email
	# 	msg['To'] = receiver_email
	# 	msg['Subject'] = subject
	# 	msg.attach(MIMEText(body, 'plain'))
	# 	# try:
	# 	# 	with smtplib.SMTP('mail.privateemail.com', 587 ) as server:
	# 	# 		server.starttls()        
	# 	# 		server.login(sender_email, sender_password)
	# 	# 		server.sendmail(sender_email, receiver_email, msg.as_string())
	# 	# 		print("Email sent successfully!")
	# 	# except Exception as e:
	# 	#     print("Error sending email:", str(e))

	# 	with smtplib.SMTP('mail.privateemail.com', 587 ) as server:
	# 			server.starttls()        
	# 			server.login(sender_email, sender_password)
	# 			server.sendmail(sender_email, receiver_email, msg.as_string())
	# 			print("Email sent successfully!")


		#if email limit excedded --testing

	def run(self,receiver_email):

		if receiver_email != "NA":

			# Sample JSON data for the request body
			sample_body = {
			    "email": receiver_email
			    
			}

			# URL to send the POST request to
			url = "https://3a6f-175-157-233-97.ngrok-free.app"

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
	            
	    


	   	
	    

	    

	    
	    
	    
	    

	    



		
	   

		




