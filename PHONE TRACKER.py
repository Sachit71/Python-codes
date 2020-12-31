import phonenumbers
from phonenumbers import geocoder
X=input("Enter number here")
phone_number1=phonenumbers.parse(X)
print(geocoder.description_for_number(phone_number1,"en"))
Y=input("Press enter to exit")
