#!/usr/bin/python

import mysql.connector

def connect():
	mydb = mysql.connector.connect(host="34.215.84.191",user="root",passwd="redhat",database="dell")
	return mydb
mydb=connect()
