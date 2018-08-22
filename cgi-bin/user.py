#!/usr/bin/python2
import cgi
import cgitb
#cgitb.enable()
#print("content-type: text/html")
#print("")
import Cookie, os, time
cookie = Cookie.SimpleCookie()

cookie_string = os.environ.get('HTTP_COOKIE')
cookie.load(cookie_string)
username=cookie['userID'].value
#print username
