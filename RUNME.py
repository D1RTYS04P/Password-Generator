from PASSGEN import passgen
from PASSGEN2 import passgen2
from PASSGEN3 import passgen3

print("Please Choose a Option")
print("1. Generate Password")
print("2. Custom Password Simplified")
print("3. Custom Password")

X = input()

if X == "1":
    passgen3()
elif X == "2":
    passgen2()
elif X == "3":
    passgen()
else:
    print("Please Pick A Valid Option!")
