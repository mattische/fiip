from flask import Flask
import sqlite3 as sql


con = sql.connect('db/db.db')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Set ip:<br>GET request: THIS-IP/setip/<your-ip> <br>Show ip:<br>GET request: THIS-IP/showip'


@app.route('/setip/<ip>')
def set_ip(ip):
    cur = con.cursor()

    if len(ip) > 9:
        cur.execute("INSERT INTO Ips (ip, date) VALUES('" + ip + "',datetime('now'))")
        return "srv.py: ip (" + ip + ") saved"
    else:
        return "not valid ip"


@app.route('/showip/')
def show_ip():
    cur = con.cursor()
    cur.execute("SELECT * FROM Ips DESC LIMIT 100")
    rows = cur.fetchall()
    ip_str = ""
    for row in rows:
        ip_str = ip_str + str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + "<br>"


    cur.close()
    return '<strong>100 most recent:<br><br>ID  |  IP  | DATETIME</strong> <br> %s' % ip_str


def db_setup():
    cur = con.cursor()    
    cur.execute("CREATE TABLE IF NOT EXISTS Ips(id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, date TEXT)")


db_setup()

