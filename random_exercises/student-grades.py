
#author: IFIOK UDOH
#date created: 27th Feb. 2020 5am

print ""
print ""
print ""
print "Hello Teacher, welcome to Student Grades App"
print "======================================="
print ""
print ""

try:
    studentCount = input("Kindly input the number students in your class : ")
    studentCount = int(studentCount)

    #if not type(studentCount) is int :
except:
    print "******You inputed a non-numeric value. Kindly restart the program and input a numeric value.************* "
    print ""
    exit()

print "======================================="
print ""
print ""

cnt = 1
studentGradesMap = {}

while studentCount >= cnt:
    print "======================================="
    name = raw_input("Input the name of student number " + str(cnt) + " : ")
    grade = raw_input("Input the score of student number " + str(cnt) + " : ")

    studentGradesMap[name] = int(grade)

    cnt = cnt + 1
    


print "======================================="
print ""
print ""


lowestScore = 100
highestScore = 0
lowestStudentInfo = []
highestStudentInfo = []

for x,y in studentGradesMap.items() :
    
    if y < lowestScore :
        lowestScore = y
        lowestStudentInfo = [x,y]
        
    if y > highestScore :
        highestScore = y
        highestStudentInfo = [x,y]


print ""
print ""
print "=================================="
print "The Student with the highest score is : " + highestStudentInfo[0] + " with a score of : " + str(highestStudentInfo[1])
print "The Student with the lowest score is : " + lowestStudentInfo[0] + " with a score of : " + str(lowestStudentInfo[1])
print "=================================="
print ""
print ""




