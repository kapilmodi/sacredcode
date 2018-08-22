#!/usr/bin/python2

import user,datetime
import cgi
import cgitb
import subprocess as sp
cgitb.enable()
import os
import db
#print("content-type: text/html")
#print("")
form = cgi.FieldStorage()
comment = form.getvalue('comment')
pname=form.getvalue('pname')

#s=sp.getstatusoutput("sshpass -p redhat ssh  -o stricthostkeychecking=no root@52.66.188.152 \"python /var/www/cgi-bin/submitfunction.py\" '{0}' {1}".format(comment,pname))

import socket

target="34.220.181.66"

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#print "Comment Entered By {0} is :{1}".format(user.username,comment)
#print "<br /> <br /> Product Name is </body>",pname
client.connect((target, 9999))

# send some data (in this case a HTTP GET request)
comment=comment.encode()
client.send(comment)

# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)
response = response.decode()
#print "<h2> Corresponding Sentiment "
#print float( response)
response=float(response)
response= round(response)
mycursor = db.mydb.cursor()
mycursor.execute("Select uid from login where emailid='{0}'".format(user.username))

userid=mycursor.fetchall()
userid=userid[0][0]
date=str(datetime.datetime.today()).split()[0]
sql = "INSERT INTO issue (uid, issue, status,dop,sentiment) VALUES ('{0}', '{1}',0,'{2}',{3})".format(userid,comment,date,response)
mycursor.execute(sql)
db.mydb.commit()
#print "Successfully Added to issue table"
#print "Dataset entry remaining"


print("Location: mail.py")
print("")
