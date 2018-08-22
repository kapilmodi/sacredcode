#!/usr/bin/python2
import smtplib
import user
sub='Complaint Registered'
content='Thank you for contacting our support services. Your request has been registered with us successfully. We will get back to you shortly with the solution to your problem.\nThank You!'
msg='Subject: {}\n\n{}'.format(sub,content)

from_email='dellteam2018@gmail.com'
from_pass='dellteam123'

to_email=user.username

mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login(from_email,from_pass)

mail.sendmail(from_email,to_email,msg)

mail.close()
print "Location: previous.py"
print ""
