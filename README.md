# fiip

A quick fix to startup wifi on my RPi and then send the ip to a server flask app that stores that info in database.
Since my RPi does not have the same ip (dynamic).

## client
Requirements:
- pip and httplib2

The script in client should be placed on the host that you wish know ip. I.e your RPi.
Run the script in intervalls, say every hour, with supervisord (http://supervisord.org/). The script requires sudo-rights since it queries on of the machines network interfaces.

## server
Requirements:
- pip
- flask

Place the script in server on a host that has an static ip and is reachable from client.
I use supervisord to run it at startup.

Here is an example of a config file for supervisor;
´´´
[program:fiip-server]   
command=python -m flask run --host=0.0.0.0   
directory=/home/userName/folder/subFolder/fiip/server   
autostart=true   
autorestart=true   
startretries=3   
stderr_logfile=/var/log/fiip-server/server.err.log   
stdout_logfile=/var/log/fiip-server/server.out.log   
user=userName   
environment=FLASK_APP='srv.py'   
´´´


This config file is created at: <code>/etc/supervisor/conf.d/fiip-server.conf</code>.
Do not forget to create folder for logfiles, as above; <code>mkdir -p /var/log/fiip-server</code>

Start supervisor;
<code>sudo service supervisor start</code>

And make supervisor read you config file;
<code>
supervisorctl reread
supervisor update
</code>

Look for any changes in the log-files.
