# coding: UTF-8

import smtplib
import os
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 


def send_mail(mail_host, mail_port, mail_from, mail_to, msg):
	# connect smtp server, set debug to see reply information
	smtp = smtplib.SMTP()
	smtp.connect(mail_host, mail_port)
	smtp.set_debuglevel(1)
	# send mail
	smtp.sendmail(mail_from, mail_to, msg.as_string())
	# quit
	smtp.quit()

def get_massage(mail_from, mail_to):
	msg = MIMEMultipart('alternative')
	# from, to, subject
	msg["From"] = mail_from
	msg["To"] = ";".join(mail_to)
	msg['Subject'] = r"Oooooooooooooooops"
	# html
	html = """\
	<html>
		<head><meta charset="UTF-8"></head>
		<body>
			<p>Hello, World!</p>
			<p>The attach is the script to send this email.</p>
		</body>
	</html>
	"""
	content = MIMEText(html, 'html', 'UTF-8')
	msg.attach(content)
	# attach
	dirname = os.path.dirname(__file__)
	filename = "send.py"
	full_filename = os.path.join(dirname, filename)
	
	attach = MIMEText(open(full_filename, "rb").read(), "base64", "UTF-8")
	attach['Content-Type'] = 'application/octet-stream'
	attach['Content-Disposition'] = 'attachment; filename=%s' % filename
	msg.attach(attach)
	# end
	return msg

if __name__ == "__main__":
	# host:port 
	mail_host = "xxx.xxx"
	mail_port = 25
	# mail from and mail to
	mail_from = "master@example.com.cn"
	mail_to = ["xxx@xxx.xxx"]
	# massage
	msg = get_massage(mail_from, mail_to)
	# send
	send_mail(mail_host, mail_port, mail_from, mail_to, msg)
