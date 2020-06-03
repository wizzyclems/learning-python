

#below stores the number of rows
rows = 2

while (rows % 2) == 0 :
   #User should input number of rows
   rows = int(raw_input("Input an odd number for rows : "))
  
   
#below variable determines the longest column
marker = int(rows/2) + 1

#Below determines the number of * to print for each row
levelCounter = 1

#Below identifies where the longest column is reached
marker_reached = False

while rows > 0 :

  columns = levelCounter

  whitespace = marker - columns
  while whitespace > 0 :
      print " ",
      whitespace = whitespace - 1

  #determines how many * really needs to be printed from left to right
  columns = columns + (columns - 1)
  while columns > 0 :
    print "*",

    columns = columns - 1

  if (levelCounter >= marker) or marker_reached :
    levelCounter = levelCounter - 1
  else :
    levelCounter = levelCounter + 1

  if levelCounter == marker: marker_reached = True

  
  rows = rows - 1
  print ""

