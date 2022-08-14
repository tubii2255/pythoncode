print('hi, this is a program that will show a 10 digit phone number')

def phone(number):

    if len(number) != 10 :
        return False
    for i in range(0,10):
        if not number[i].isdecimal():
            return False
    return True


message = input()
found = False
for i in range(len(message)):
    num = message[i:i+10]
    if phone(num):
        print('phone number found \n' + num)
        found = True
if not found:
    print(" sorry couldn't find the number ")
