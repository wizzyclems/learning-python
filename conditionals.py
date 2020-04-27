
#Python uses whitespace indentation to define code blocks
#Failure to do this will cause an error in your python code

age = 17
gender = "male"

if age <= 17:
  print "You are a teenager"



if age > 17:
  print "You are an adult"
else:
  print( "You are just a teenager.")



if age < 17 and gender == 'male':
  print("You are a male teenager")
elif age < 17 and gender == 'female':
  print "You are a female teenager"
else:
  print("I don't know what you are")


if age <= 17:
  print("You are a teenager")
  if gender == 'male':
    print("You are a young man")
  else:
    print("You are a young woman")
else:
  print("You are not young")


#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#"pass" is a keyword in python
if age > 17:
  pass



 
