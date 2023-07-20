import smtplib
from st2common.runners.base_action import Action

class SendMessageToSlackAction(Action):
	# creates SMTP session
	def run(self,receiver_email="test",message="test message"):
		s = smtplib.SMTP('smtp.gmail.com', 587)

		# start TLS for security
		s.starttls()

		# Authentication
		s.login("sender_email_id", "sender_email_id_password")


		# sending the mail
		s.sendmail("sender_email_id", receiver_email, message)

		# terminating the session
		s.quit()
