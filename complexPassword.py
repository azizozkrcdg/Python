# you can generate secure and complex password by running this code

import random
import string

numbers = string.digits
symbols = string.punctuation
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
allCharacters = [numbers, symbols, lowerCase, upperCase]

password = ""

for i in range(4):
    for j in range(4):
        password += allCharacters[j][random.randint(0,9)]

password = list(password)
random.shuffle(password)

newPassword = ""

newPassword = newPassword.join(password)
print(newPassword)