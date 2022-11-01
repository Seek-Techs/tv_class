import string
import random

password = str
userchoice = int(input())
userlength = int(input())

if userchoice == 1:
    password = ''
    for i in range(userlength):
        password += random.choice(string.ascii_letters)

else:
    password = ''
    for i in range(userlength):