### Sending anonymous email using smtplib in python

Homework on Information Security lesson: send a fake(anonymous) E-mail using a fake "mail from".



Suppose that you want to send a fake email to ryan@meow.com

Firstly, using "nslookup" command to find the exchange server of "meow.com" (`set type=mx`)

Coz SMTP protocol doesn't authorize on exchange server, you can directly send MIME format E-mail to the exchange server.


Tips: Testing it on your own email to make sure your E-mail won't be sent to Trash.


Ryan
2013/6/19
