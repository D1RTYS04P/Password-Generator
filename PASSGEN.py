import random

def passgen():
    def passtostring(password2):
        str1 = ""
        for ele in password2:
            str1 += ele
        return str1

    def chartostring(allcharacters):
        str2 = ""
        for ele in allcharacters:
            str2 += ele
        return str2

    def captostring(caplist):
        str3 = ""
        for ele in caplist:
            str3 += ele
        return str3

    def lowertostring(lowerlist):
        str4 = ""
        for ele in lowerlist:
            str4 += ele
        return str4

    def numtostring(numlist):
        str5 = ""
        for ele in numlist:
            str5 += ele
        return str5

    def spetostring(spelist):
        str6 = ""
        for ele in spelist:
            str6 += ele
        return str6

    def cap():
        for a in range(capnum):
            caprn = str(input().upper())
            caplist.append(caprn)

    def lower():
        for a in range(lowernum):
            lowerrn = str(input().lower())
            lowerlist.append(lowerrn)

    def num():
        for a in range(numnum):
            numrn = str(input().lower())
            numlist.append(numrn)

    def spe():
        for a in range(spenum):
            spern = str(input().lower())
            spelist.append(spern)

    length = int(input("Please Enter Password Length: "))


    caplist = []
    capnum = int(input("How Many Capital Letters Would You like? (No Spaces) "))
    print("Please Add Them Individualy One By One")
    cap()


    lowerlist = []
    lowernum = int(input("How Many Lowercase Letters Would You like? (No Spaces) "))
    print("Please Add Them Individualy One By One")
    lower()


    numlist = []
    numnum = int(input("How Many Numbers Would You like? (No Spaces) "))
    print("Please Add Them Individualy One By One")
    num()


    spelist = []
    spenum = int(input("How Many Special Characters Would You like? (No Spaces) "))
    print("Please Add Them Individualy One By One")
    spe()

    allcharacters = []
    allcharacters += caplist
    allcharacters += lowerlist
    allcharacters += numlist
    allcharacters += spelist

    password1 = []

    for a in range(length):
        randomchar = random.choice(allcharacters)
        password1.append(randomchar)

    password2 = ''.join(''.join(p) for p in password1)

    print(passtostring(password2))
