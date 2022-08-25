
totel = 0
print('hi welcome to my expense calculator.. ')
def addmoney():         #adding money to total balance
    global totel
    mo = int(input('add your  money here\n'))
    totel += mo
    print (f'{totel} , is your current balance')
    return totel


def ask_to_add(totel):
    while True:                    
        ans =  input("do u want to add more\nyes or no\n")
        if ans.lower() == 'yes':
            
            addmoney()
        elif ans.lower() == 'no':
            break
        else:
            print('YES OR NO')


def subtrac():
    
    global totel
    print('please enter the values seperated with space not with commas or anything')
    #substracing from totel balance
    
    mo = list(map(int, input('enter your expenses to be substract,\n').split()))
    for i in mo:
        a=0
        a += i
        totel -= a
    
    print(f'{totel} , is your current balance')


    


def ask_substract():
    global totel
    while True:
        answ = input('do you want to substract\nyes or no\n')
        if answ.lower() == 'yes':
            subtrac()
        elif answ.lower() == 'no':
            print('thanks')
            print(f'{totel} , is your current balance')
            break
        else:
            print('YES OR NO')

totel = addmoney()
ask_to_add(totel)
ask_substract()

