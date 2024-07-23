import random
import string

Numbers=[]
User=[]

#UserVerficationcode function
def VerificationCode():
    values = string.ascii_letters + string.digits + string.punctuation

    values = list(values)
    key = values.copy()

    random.shuffle(key)
    for x in key[0:5]:
        Numbers.append(x)

    store=''.join(Numbers)
    print("Verification code is:",store)

    #get user input and verfication process

    userInput=str(input("Paste that code here: "))
    print()
    if store==userInput:
        print("User Login Succsesful !")
    else:
        print("User Login unsuccesful !")

#User registation front end

print('----------------------------------------------')
print("           Welcome to ICBT Moodle             ")
print('----------------------------------------------')
print()
phone_numbers = [783592300, 783653455, 702477188, 1]
phoneNumber = int(input("Please enter your phone number: "))
NumberFound = False
for x in phone_numbers:
    if x == phoneNumber:
        VerificationCode()
        NumberFound = True
        break;
if not NumberFound:
    print("This number is not registered")