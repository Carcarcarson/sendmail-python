Send email using smtplib in python

Homework on information Security class, send a fake email using a fake "mail from"

---------------------------------------------------------------------

Suppose that you want to send a fake email to ryan@meow.com

Firstly, using "nslookup" to find the exchanger server of "meow.com" (set type=mx)

Coz smtp don't auth on exchanger server, you can simply send MIME format email to ryan@meow.com

Tips: Testing it on your own email to make sure it won't be sent to Trash


Ryan
2013/6/19
