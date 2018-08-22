#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
print("content-type: text/html")
print("")

import Cookie, os, time
cookie = Cookie.SimpleCookie()

cookie_string = os.environ.get('HTTP_COOKIE')
cookie.load(cookie_string)
username=cookie['userID'].value


print("""
<h2>Welcome {}
</h2>
<br />
Hope you are enjoying our products and services , If not, then please help us improve our services by lodging a complain! 

<br />
<br />
<a href=../web/comment.html>Report a Problem</a>
<br />
<br />
<a href=previous.py>Previous History</a>
""".format(username))

