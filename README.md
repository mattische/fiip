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
