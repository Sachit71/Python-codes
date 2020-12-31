import string
import random

X=input("Press enter")

def generatePassword(num):
    password=""

    for n in range(num):
        x=random.randint(0,94)
        password+=string.printable[x]
        
    return password

print("Your password is",generatePassword(16))
Y=input("Press enter to exit")
Y=str(Y)


