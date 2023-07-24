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

		
	    # Set up the MIMEText object for the email content
	    msg = MIMEMultipart()
	    msg['From'] = sender_email
	    msg['To'] = receiver_email
	    msg['Subject'] = subject

	    # Attach the email body
	    msg.attach(MIMEText(body, 'plain'))

	    # Connect to the SMTP server
	    try:
	        with smtplib.SMTP('mail.privateemail.com', 587 ) as server:  # Replace with your SMTP server and port
	            server.starttls()
	            # Log in to the SMTP server
	            server.login(sender_email, sender_password)

	            # Send the email
	            server.sendmail(sender_email, receiver_email, msg.as_string())
	            print("Email sent successfully!")

	    except Exception as e:
	        print("Error sending email:", str(e))


		




