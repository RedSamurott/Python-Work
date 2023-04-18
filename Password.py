######################
#
# Password.py
#
# Author: Donald Summers
#
# Description: Lab Assignment 6 Part 1, Passwrod
#
# A way to verify a hardcoded password by randomizing the digits entered that translates to the actual password
#
# Example use: python Password.py
#
# Code sampled from Doug Galarus
######################
import random

#sets up PIN and converted numbers for PIN
pin = [4,5,1,1,4]
randNumbers = [random.randint(1,3) for x in range(10)]

#converts PIN variable into converted PIN
for converted in range(len(randNumbers)):
    for unconverted in range(len(pin)):
        if pin[unconverted]==converted:
            pin[unconverted]=str(randNumbers[converted])

#gets the users supposed PIN with a bit of UI
print("PIN: 0 1 2 3 4 5 6 7 8 9")
print("NUM:",*randNumbers)
print("")
pinInput = list(input("Please enter your converted password: "))
print("")

#checks to see if the PIN input is the same as the converted PIN
if pin==pinInput:
    print("Welcome! You are correct.")
else:
    print("Sorry, that password is incorrect.")