import time
x=""
def ab():
	x='Set-Cookie: lastvisit=' + str(time.time());
	x+='Content-Type: text/html\n'
	x+='<html><body>'
	x+='Server time is'
	x+='</body></html>'	
	return(x)
