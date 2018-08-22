#!/usr/bin/python3
import  os, time

import matplotlib.pyplot as plt
import cgi
import cgitb
import os,sys

cgitb.enable()


print("content-type: text/html")
print("")
x=5
x+=1
print(x)
print( "<h1>Hello World")
cookie_string = os.environ.get('HTTP_COOKIE')
cookie.load(cookie_string)
print(cookie)

print("sfd")
"""
# set HOME environment variable to a directory the httpd server can write to
os.environ[ 'HOME' ] = '/tmp/'
import matplotlib
# chose a non-GUI backend
matplotlib.use( 'Agg' )

import pylab

#Deals with inputing data into python from the html form
#form = cgi.FieldStorage()

# construct your plot
#pylab.plot([1,2,3])

print("Content-Type: image/png\n")

# save the plot as a png and output directly to webserver
#pylab.savefig( sys.stdout, format='png' )
"""
