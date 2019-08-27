from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector
from hashlib import md5

app = Flask(__name__)
app.secret_key = '1234'
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='school'
)
@app.route('/', methods = ['GET'])
def homepage():
    return render_template ('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    body = request.form
    used = db.cursor()
    used.execute('select * from accounts')
    data = used.fetchall()
    email_temp = []
    for item in data:
        email_temp.append(item[2])
    for item in data:
        if body['email'] not in email_temp:
            used = db.cursor()
            qry = 'insert into accounts (email,password) values (%s, %s)'
            val = (body['email'], body['password'])
            used.execute(qry, val)
            db.commit()
            return 'sign up success!'
        else:
            return 'email already exist!'

@app.route('/signin', methods=['POST','GET'])
def signin():
    body = request.form
    used = db.cursor()
    used.execute('select * from accounts')
    data = used.fetchall()
    email_temp = []
    for item in data:
        email_temp.append(item[2])
    for item in data:
        if body['email'] not in email_temp:
            return jsonify({'status': 'email tidak terdaftar!'})
        else:
            if item[2] == body['email']:
                if item[1] == body['password']:
                    return jsonify({'status': 'SUKSES!'})
                else:
                    return jsonify({'status': 'salah password!'})




if __name__ == "__main__":
    app.run(
        debug = True,
        host = '0.0.0.0',
        port = 5678
    )