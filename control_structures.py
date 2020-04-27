
cnt = 0
salary = 0.0


while cnt < 5:
 salary += 200
 cnt = cnt + 1


print "After 5 trials, the new salary is : " + str(salary)



print ""
print "====================================="
print ""


#This while loop takes advantage of the break construct to interrupt the loops iteration when a certain condition is met.
cnt = 1
salary = 0.0

while cnt < 10:
 salary += 200
 
 if cnt > 5:
  break

 cnt = cnt + 1


print("The counter is : " + str(cnt) + ", the salary is : " + str(salary))

print ""
print "====================================="
print ""


#Below while loop takes advantage of the continue construct to skip some iterations of the loop
cnt = 1
salary = 0.0

while cnt < 10:
 if cnt % 2 != 0:
  #print "This should be an odd number : " + str(cnt)
  cnt = cnt + 1
  continue

 print "Yay! An even number : " + str(cnt)
 cnt = cnt + 1


print ""
print "====================================="
print ""


#For loop in python is more about iteration over a sequence.
#It does not require index variables as is the case in other programming languages
fruit_bag = ["banana","apple","quava","eggplant"]

for fruit in fruit_bag:
  print(fruit)













