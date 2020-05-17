

#You define functions in python using the def keyword followed by the function name and parenthesis
#Naming a function follows the same rule as variable naming.
def greetings():
  print("Hello, Good morning to the world of us.")


#functions can also take in parameters. These are extra data passed to the function to perform operations on them. See example below.
#Correct number of arguments must be passed to a function
def showName(name):
 print("Your name is : " + name)



showName("hillary")

print ""
print "======================"
print ""

#Python allows you to define functions that accept arbitrary number of arguments
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#You can also access the parameter values the same way you access list values using []
def allStudent(*arg):
  for a in arg:
     print a


allStudent("Jameson","Dariel","Pilot","Filament")

print ""
print "======================"
print ""

#Function arguments can be specified in a key value pair
#This allows you to specify the parameters without following their defined order
def mapDetails(city,country):
   print("City : " + city)
   print("Country : " + country)


mapDetails(country = "Belarus",city = "Ipaju")
 
print ""
print "======================"
print ""

#Python also allows you to specify arbitrary key-value parameters as shown below
#You achieve this by specifying 2 astericks in front of the argument
def arbKeyValue(**kid):
  print("His last name is " + kid["lname"])

arbKeyValue(fname = "Tobias", lname = "Refsnes")


print ""
print "======================"
print ""

#functions in python also specify default values for parameters for cases where they user forgets/chooses not to provide one
def showCountry(countryName="Nigeria"):
  print "Your country name is : " + countryName



showCountry("America")
showCountry("Britain")
showCountry()
showCountry("Austria")


print ""
print "======================"
print ""



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


print ""
print "======================"
print ""


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



