#!/usr/bin/python3

import db, cgi
form = cgi.FieldStorage()
uid = form.getvalue('uid')
iid=form.getvalue('iid')

#print("content-type: text/html")
#print("")
#print(uid,iid)
mycursor = db.mydb.cursor()
sql = "UPDATE issue SET status = 1  WHERE iid ={} ".format(iid)
mycursor.execute(sql)
db.mydb.commit()
def issueResolved(uid,iid):
    mydb = mysql.connector.connect(host="34.215.84.191",user="root",passwd="redhat",database="dell")
    mycursor = mydb.cursor()
    sql = "Select * from dataset where uid='"+uid+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    sql3="SELECT datediff((Select dor from issue where iid="+str(iid)+"),(Select dop from issue where iid="+str(iid)+"))"
    mycursor.execute(sql3)
    myresult3 = mycursor.fetchall()
    a=[0 for i in range(7)]
    a[1]=myresult[0][1]
    a[2]=myresult[0][2]
    a[3]=((myresult[0][1]+myresult[0][2])*myresult[0][3]+(myresult3[0][0]))/((myresult[0][1]+myresult[0][2])+1)
    a[4]=myresult[0][4]
    a[5]=myresult[0][5]
    a[6]=myresult[0][6]
    a[2]-=1
    a[1]+=1
    a[6]=predict(a[1:6])
    print(a)
    sql="UPDATE dataset set ir=ir+1,iu=iu-1 ,ati="+str(int(a[3]))+",sentiment="+str(int(a[6]))+" where uid='"+myresult[0][0]+"'"
    mycursor.execute(sql)
    mydb.commit()
issueResolved(uid,iid)
print("Location: previous.py")
print("")

