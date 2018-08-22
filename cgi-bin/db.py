#!/usr/bin/python

import mysql.connector

def connect():
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="redhat",database="dell")
	return mydb
mydb=connect()
