


word = "my. testedt! days- of hope"

print("The word is {}".format(word))

for w in word :
    word = word.replace(".","")
    word = word.replace("!","")
    word = word.replace("-","")


print("The new word is {}".format(word))