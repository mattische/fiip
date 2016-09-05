from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/showip/<ip>')
def show_ip(ip):

    return 'Ip: %s' % ip
