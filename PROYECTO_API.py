from flask import Flask,render_template,request,redirect,url_for, session, flash
import mysql.connector as mysql

app = Flask(__name__)

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)


@app.route('/')
def Index():
    return render_template('index.html')