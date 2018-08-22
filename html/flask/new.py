from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response
from hashlib import md5
import hello
import mysql.connector
import socket
import time
app = Flask(__name__)

#######################
#   DATABASE CONFIG   #
#######################

#db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
db= mysql.connector.connect(host="localhost",user="root",passwd="redhat",database="dell")

cur = db.cursor()

@app.route('/')
def index():
    
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        """
        name = request.cookies.get('userID')
        print(name)
        """
        #return render_template('index.html', session_user_name=username_session)
        return redirect("http://34.215.84.191/web/user.html", code=302)
    else:
        return redirect(url_for('login'))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    error = None
    if 'username' in session:
        if request.method == 'POST':
            comment  = request.form['comment']
            pname  = request.form['pname']
            return render_template('submit.html')

    #return redirect(url_for('logout'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username_form  = request.form['username']
        password_form  = request.form['password']
        cur.execute("SELECT COUNT(1) FROM login WHERE emailid = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM login WHERE emailid = %s;", [username_form]) # FETCH THE HASHED PASSWORD
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']
                    resp = make_response(render_template('index.html'))
                    resp.set_cookie('userID', username_form)
                    time.sleep(1)
                    return resp
                    #return redirect(url_for('index'))
                else:
                    error = "Invalid Credential"
        else:
            error = "Invalid Credential"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register')
def register():
	#return redirect("http://52.66.188.152/cgi/hello.py", code=302)
	return render_template('user.html')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
