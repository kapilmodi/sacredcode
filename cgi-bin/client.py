#!/usr/bin/python3
import cgi,cgitb

import socket
#target = '{}.{}.{}'.format(hostname, sld, tld)
target="34.220.181.66"

print("content-type: text/html")
print("")
# receive the response data (4096 is recommended buffer size)
# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("fsds")
# connect the client
# client.connect((target, port))
client.connect((target, 9999))
print("dfsdf")
# send some data (in this case a HTTP GET request)
client.send(b"hello")
print("content-type: text/html")
print("")
# receive the response data (4096 is recommended buffer size)
response = client.recv(4096)
response = response.decode()
print( response)
