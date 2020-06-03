import os
import datetime

filepath = os.path.join(os.getcwd(),"coursera","elevator.py")
file = open(filepath)
file.
if os.path.exists(filepath) :
    print "this is some fun"
    print os.path.getsize(filepath)
else:
    print "The file does not exist"

print os.getcwd()


print datetime.datetime.fromtimestamp(os.path.getmtime(filepath)).date()

