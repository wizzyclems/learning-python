class Student:

  name = ""
  age = ""
  gender = ""

  def __init__(self):
      pass
  

 # def __init__(self,name,age,gender):
  #  self.name = name
   # self.age = age
    #self.gender = gender


  def getName(self):
    return self.name


  def getAge(self):
    return self.age 


  def getGender(self):
    return self.gender

  def showDetails(self):
      print "Name: " + self.getName()
      print "Age: " + str(self.getAge())
      print "Gender: " + self.getGender()




student = Student()
student.name = "Darren"
student.age = 20
student.gender = "Male"

student.showDetails()


#YOu can delete an object property using the "del" keyword
del student.name

print "The name variable after being deleted : " + student.name


#You can also delete and object instance also using the "del" keyword
del student

print "Using the student object after deleting it : " + student.getGender




