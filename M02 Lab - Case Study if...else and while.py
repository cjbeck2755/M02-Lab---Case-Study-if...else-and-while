#M02 Lab - Case Study: if...else and while
#C.J. Becker
#1/29/2024
#Python 3.8.10
#test to see if a GPA is good enough to make the dean's list and the honor roll

import sys

lastName = str(input("Enter last name: "))
if (lastName == "ZZZ"):
    sys.exit()
    
firstName = str(input("Enter first name: "))
GPA = float(input("Enter GPA: "))
if (GPA >= 3.5):
    print("You made the dean's list")
if (GPA >= 3.25):
    print("You made the honor roll")
else:
    print("You did not make either list")