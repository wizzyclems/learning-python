
#Python does not have inbuilt arrays,instead you use the python lists for your arrays.
#Arrays are variables that can store more than a single value at the same time.
usernames = ["Jamiu","Dariel","Quava","Baptist","Timi"]
you = "Dar"

print("is it there : " + you in usernames)
for name in usernames:
   print(name)


print ""
print "====================="
print ""

cnt = 0

print("The length of the array 'usernames' is : " + str(len(usernames)))
print("See the names below...")

while cnt < len(usernames):
    print usernames[cnt]
    cnt = cnt + 1

print ""
print "====================="
print ""


print usernames.pop()
print usernames.append("Dummy")
print usernames.remove("Dummy")



