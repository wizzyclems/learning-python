

#Variables are containers for storing data values.
#You store these values so you can re-use them within your program
#Unlike other programming languages, Python does not have data type definition for variables.
#A variable is created the moment you first assign a value to it.


#Below code declares an integer variable "counter" and assigns a value of 10 to it.
counter = 10


#Below declares a floating point integer variable
account_balance = 2530.43



#String variables can be declared either by using single or double quotes
first_name="Jameson"
surname='Tencent'


#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

#2sure = "someones name"

#print("Someone's name is " + 2sure)


#Python allows you to assign values to multiple variables in one line
x, y, z = 30,20,40

print("The value of variables x, y and z is shown below:")
print x
print y
print z


#you can assign the same value to multiple variables in one line
x=y=z=40

print("The new values for variables x, y and z is shown below:")
print x
print y
print z

#You can join two variables together using the "+" sign
firstname = "Jamiue"
surname = "Danzaki"

print(firstname + surname)

#The "+" operator works as addition while being used with numeric variables
wage1 = 20
wage2 = 30
total_wage = wage1 + wage2

print(total_wage)

#You cannot use the "+" operator to join a string with a number. Below line throws an exception
#print("Your total wage is : " + total_wage)



#Global Varibles
#Variables that are created outside of a any functions.
#All the variables we have created so far are all global variables
#Global variables can be used by everyone, both inside of functions and outside.
surname = "Daniel"

def changeSurname():
  print "The surname inside the function changeSurname is " + surname


changeSurname()

print "The surname in the code is : " + surname


#You can define a variable inside a funciton with the same as a global variable
#The variable inside the function overwrites the global variable when referenced from the function
firstname = "Queen"

def changeFirstname():
  firstname = "Darling"
  print("This is the variable firstname inside the function : " + firstname)


changeFirstname()

print ("This is the variable firstname globally : " + firstname)


#Use the "global" keyword if you want to change the value of a global variable inside a function
#Use the "global" keyword if you want to declare a global variable inside a function
# Take not to not initialize your global variable in the same statement
globe = "worldly"

def createGlobalVariable():
  global global_variable
  global_variable = "I am global"
  global globe
  globe = "changed world"
  

createGlobalVariable()

print("The value of globe was change inside the function. The new value is : " + globe)
print("Global variable value defined in the function is : " + global_variable)


  


























