import smtplib
from st2common.runners.base_action import Action
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMessageToSlackAction(Action):
	# creates SMTP session
	def run(self,receiver_email):

		sender_email=self.config['sender_email']
		sender_password = self.config['sender_password']
		subject = self.config['subject']
		body = self.config['body']
		msg = MIMEMultipart()
		msg['From'] = sender_email
		msg['To'] = receiver_email
		msg['Subject'] = subject
		msg.attach(MIMEText(body, 'plain'))
		# try:
		# 	with smtplib.SMTP('mail.privateemail.com', 587 ) as server:
		# 		server.starttls()        
		# 		server.login(sender_email, sender_password)
		# 		server.sendmail(sender_email, receiver_email, msg.as_string())
		# 		print("Email sent successfully!")
		# except Exception as e:
		#     print("Error sending email:", str(e))

		with smtplib.SMTP('mail.privateemail.com', 587 ) as server:
				server.starttls()        
				server.login(sender_email, sender_password)
				server.sendmail(sender_email, receiver_email, msg.as_string())
				print("Email sent successfully!")
	            
	    


	   	
	    

	    

	    
	    
	    
	    

	    



		
	   

		




