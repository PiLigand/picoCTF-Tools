#LongString.py
#Prepared to quickly make strings to complete the picoCTF 2017 challenge "looooooong"

import sys

if((len(sys.argv) > 1) and ((len(sys.argv)-1)%2 == 0)):
    str = ""
    for n in range(1, len(sys.argv), 2): #Cycles through arguments in pairs. First a number of iterations, then a character to be iterated
        for y in range(0, int(sys.argv[n])):
            str = str + sys.argv[n+1]
            #print(sys.argv[n+1])
    print(str)
else:
    print("Uneven number of or too few arguments")
