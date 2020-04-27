# We're working with a list of flowers and some information about each one. 
# The create_file function writes this information to a CSV file. 
# The contents_of_file function reads this file into records and returns the information 
# in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn 
# the data in the CSV file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # # Open the file
  # flowers = []
  # file = open(filename)
  # csv_f = csv.DictReader(file)
    
  # # Read the rows of the file into a dictionary
  # for c in csv_f:
  #   flower = {}
  #   flower["name"] = c["name"]
  #   flower["color"] = c["color"]
  #   flower["type"] = c["type"]
  #   flowers.append(flower)

   # Open the file
  flowers = []
  file = open(filename)
  csv_f = csv.reader(file)
  row_count = 0
    
  # Read the rows of the file into a dictionary
  for c in csv_f:
    
    if row_count == 0 :
      row_count += 1
      continue
    
    flower = {}
    flower["name"] = c[0]
    flower["color"] = c[1]
    flower["type"] = c[2]
    flowers.append(flower)

  # Process each item of the dictionary
  for f in flowers:
    return_string += "a {} {} is {}\n".format(f["color"], f["name"], f["type"])

  return return_string


#Call the function
print(contents_of_file("flowers.csv"))


# import os
# import csv

# # Create a file with data in it
# def create_file(filename):
#   with open(filename, "w") as file:
#     file.write("name,color,type\n")
#     file.write("carnation,pink,annual\n")
#     file.write("daffodil,yellow,perennial\n")
#     file.write("iris,blue,perennial\n")
#     file.write("poinsettia,red,perennial\n")
#     file.write("sunflower,yellow,annual\n")

# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#   return_string = ""

#   # Call the function to create the file 
#   create_file(filename)

#   # Open the file
#   ___
#     # Read the rows of the file into a dictionary
#     ___
#     # Process each item of the dictionary
#     for ___:
#       return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
#   return return_string

# #Call the function
# print(contents_of_file("flowers.csv"))
