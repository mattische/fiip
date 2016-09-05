from flask import Flask
import sqlite3 as sql


con = sql.connect('db.db')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/setip/<ip>')
def set_ip(ip):
    cur = con.cursor()

    cur.execute("INSERT INTO Ips (ip, date) VALUES('" + ip + "',datetime('now'))")
    return "ok"


@app.route('/showip/')
def show_ip():
    cur = con.cursor()
    cur.execute("SELECT * FROM Ips DESC LIMIT 100")
    rows = cur.fetchall()


    return 'Ip: %s' % rows


def db_setup():
    cur = con.cursor()    
    cur.execute("CREATE TABLE IF NOT EXISTS Ips(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, date TEXT)")


db_setup()
