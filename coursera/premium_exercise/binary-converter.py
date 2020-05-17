
binaryNumberMap = {"1":1,"2":2,"3":4,"4":8,"5":16,"6":32,"7":64,"8":128}


def showActivity():
    print("====================================================")
    print("Welcome To Binary Converter Command Line App")
    print("1. Convert From Binary to Number")
    print("2. Convert From Number to Binary")
    print("3. Exit")
    print("====================================================")
    return input("Choose an Activity between 1 - 3: ")
   

def convertBinaryToNumber():
    print("")
    print("")
    print("====================================================")
    print("Converting from Binary to Number")
    binary = input("Input your Binary number:  ")
    print("You inputed the binary : " + str(binary))
    
    for b in binary:
        if b != 1 and entry != 0 :
            print("You inputed an invalid binary number. " + binary)
            break

    for idx, bit in enumerate(binary:
        if bit != 1 and bit != 0 :
            print("You inputed an invalid binary number. " + binary)
            break

        


    print("====================================================")
    print("")
    print("")


def convertNumberToBinary():
    print("")
    print("")
    print("====================================================")
    print("Converting from Number to Binary")
    number = input("Input your number:  ")
    print("You inputed the binary : " + str(number))
    print("====================================================")
    print("")
    print("")

def exitProgram():
    print("")
    print("")
    print("====================================================")
    print("You have chosen to exit this program.")
    print("Thank you for playing with us today.")
    print("====================================================")
    print("")
    print("")



stopProgram = False;

while True:
   entry = int(showActivity())
   print("")
   
   if entry != 1 and entry != 2 and entry != 3 :
       continue

   if entry == 1 :
        convertBinaryToNumber() 
   elif entry == 2 :
        convertNumberToBinary() 
   else:
        exitProgram()
        break


