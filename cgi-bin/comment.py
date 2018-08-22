#!/usr/bin/python3

import cgi
import cgitb
import os,sys

cgitb.enable()
print("content-type: text/html")
print("")

print("""
<html>
<body>
<form action='commentsubmit.py' method=GET>
Name <input type=text name='username'> 
<br />
Comment  <textarea name="message" rows="10" cols="30"></textarea>
<br />

  <br>
  <input type="submit">

</form>

</body>
</html>
""")
