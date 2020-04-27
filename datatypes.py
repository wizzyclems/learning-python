



#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview



x = "Hello World"
print("String : " + x)
print("=================")
	
x = 20
#print("Variable type is : " + type(x))
print ("int : " + str(x))
print(type(x))
print("=================")

x = 20.5
#print("Variable type is : " + type(x))
print ("Float : " + str(x))
print(type(x))
print("=================")
	
x = 1j	
#print("Variable type is : " + type(x))
print ("Complex : " + str(x))
print(type(x))
print("=================")

x = ["apple", "banana", "cherry"]	
#print("Variable type is : " + type(x))
print ("List : " + str(x))
print(type(x))
print("=================")

x = ("apple", "banana", "cherry")
#print("Variable type is : " + type(x))
print ("Tuple : " + str(x))
print(type(x))
print("=================")
	
x = range(6)
#print("Variable type is : " + type(x))
print ("Range : " + str(x))
print(type(x))
print("=================")
	
x = {"name" : "John", "age" : 36}
#print("Variable type is : " + type(x))
print ("Dict : " + str(x))
print(type(x))
print("=================")
	
x = {"apple", "banana", "cherry"}
#print("Variable type is : " + type(x))
print ("Set : " + str(x))
print(type(x))
print("=================")
	
x = frozenset({"apple", "banana", "cherry"})	
#print("Variable type is : " + type(x))
print ("frozenset : " + str(x))
print(type(x))
print("=================")

x = False	
#print("Variable type is : " + type(x))
print ("Boolean : " + str(x))
print(type(x))
print("=================")

x ="Hello"
#print("Variable type is : " + type(x))
print ("String : " + str(x))
print(type(x))
print("=================")
	
x = bytearray(5)
#print("Variable type is : " + type(x))
print ("bytearray : " + str(x))
print(type(x))
print("=================")
	
x = memoryview(bytes(5))
#print("Variable type is : " + type(x))
print ("Memoryview : " + str(x))
print(type(x))
print("=================")












