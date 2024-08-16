import random
chars='qwertyuiopasdfghjklmnbvcxzQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%&.,;'
number=input("Amount of passwords to generate:")
number=int(number)
length=input("Write your password length:")
length=int(length)
print("Here are your passwords:")
for pwd in range(number):
    passwords=''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)