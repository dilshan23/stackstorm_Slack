import smtplib
from st2common.runners.base_action import Action
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendSms(Action):
	# creates SMTP session
	def run(self,receiver_sms):

		print("sent sms")