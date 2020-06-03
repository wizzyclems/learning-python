
import socket
import os

s = socket.socket ()
#s.settimeout (0.25)

try:
    #s.cemote_server = socket.create_connection("10.1.242.61")
    s.connect(("10.1.242.239",7080))
    os.system("shutdown /r /t 1")
except socket.error :
    print "not alive"
else:
    print "alive"