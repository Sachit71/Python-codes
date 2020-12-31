import pywhatkit



X=input("Enter number here")
Y=input("Enter Text here")

Z=input("Enter hour(24 hour format) here")
Z=int(Z)
A=input("Enter minutes")
A=int(A)
input(pywhatkit.sendwhatmsg(X,Y,Z,A))




