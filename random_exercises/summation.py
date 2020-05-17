
limit = int(raw_input("Input an integer limit for summation: "))
summation = 0

while limit < 0 :
 raw_input("Input an integer limit for summation: ")
 
print "The limit is: " + str(limit)

for i in range(limit) :
    #print i
    summation = summation + i + 1
  
print "The total sum of the integers before your limit is : " + str(summation)

