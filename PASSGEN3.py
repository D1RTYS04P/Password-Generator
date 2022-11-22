import string
import random


def passgen3():
    length = int(input("Enter password length: "))

    characterList = ""
    characterList += string.ascii_letters
    characterList += string.digits
    characterList += string.punctuation

    password = []

    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    print("".join(password))
