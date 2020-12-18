import string
import random

length = int(input("Enter password length: "))
password = ""

for i in range(length):
    newChar = random.choice(string.printable)
    password = (password + newChar)

print(password)