import string
import random

def passgen2():
    length = int(input("Enter password length: "))
    
    print('''Choose character set for password from these :
             1. Digits
             2. Letters
             3. Special characters
             4. Generate Password''')
    
    characterList = ""
    
    while (True):
        choice = int(input("Pick a number "))
        if (choice == 1):
            print("Included 0-9")
            characterList += string.ascii_letters
        elif (choice == 2):
            print("Included A-Z a-z")
            characterList += string.digits
        elif (choice == 3):
            print("Included All Special Characters")
            characterList += string.punctuation
        elif (choice == 4):
            break
        else:
            print("Please pick a valid option!")
    
    password = []
    
    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
    
    print("".join(password))