#!/usr/bin/python
import db
import cgi,cgitb
import Cookie, os, time
cgitb.enable()

print("Content-type: text/html")
print("")
print """<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"><body>
<div class="w3-container">
  <h2>"""
cookie = Cookie.SimpleCookie()
print("Previous History of ")
cookie_string = os.environ.get('HTTP_COOKIE')
cookie.load(cookie_string)
username=cookie['userID'].value
print(username)
mycursor = db.mydb.cursor()
sql="select uid from login where emailid='{}'".format(username)
mycursor.execute(sql)
myresult = mycursor.fetchall()
#print("<br /><br /> Uid = ")
for i in myresult:
	username=i[0]
#print(username)
print "</h2><p align=right><a href='http://34.215.84.191:5000/logout'>Logout</a></p>"
#username='kapilmodi'
mycursor.execute("SELECT iid,issue,status FROM issue where uid='{}'".format(username))


myresult = mycursor.fetchall()
"""
for x in myresult:
  print(x[0].encode("utf-8"))
  print(x[1])
"""

print("<table class='w3-table-all w3-card-4'")
print "<tr><th>Issue Id </th><th>Issue </th><th>Status</th></tr>"
for x in myresult:
	print "<tr><td>",x[0],"</td><td>"
	print x[1].encode('utf-8')

	print "</td><td>"
	if x[2]==0 :
		print "In Progress<h5>Resolved! Click<a href=http://34.220.181.66/cgi-bin/resolve.py?uid="+username+"&iid="+str(x[0])+">Here</a></h5>"
		#print "<a href=http://34.220.181.66/cgi-bin/resolve.py?uid="+username+"&iid="+str(x[0])+">", x[2] ,"</a>"
	else:
		#print x[2]
		print "Resolved"
	print "</td>"
#	print "<tr><td>" + x[0].encode('utf-8') + "</td><td>" + x[1] "</td></tr>"
print "</table></div></body>"
