totel_balance=0
def myexpense():
    global totel_balance
    expense = True
    while expense is True:
        balance = int(input('add the amount\n'))       
        totel_balance += balance
        over = input('is that all or you want  to add more?\n')

        if over.lower() == 'no':
            print('your totel balance is\n', totel_balance)
            expense = False
            
        else:
            print('your totel balance is\n', totel_balance)
            expense = True

myexpense()
            
def mini():
    mi = True
    while mi is True:
        amount = int (input('enter the amount you want to decrease.\n'))
        global totel_balance
        totel_balance -= amount
        print("your curent balance is\n", totel_balance)
        stop = input("do you want decrease more? yes or no \n")
        if stop.lower() == 'yes':
            mi = True
        else:
            
            break
j = True
while j is True:
    expense= input('do you want to  decrese the amount\n')
    if expense.lower() ==  'yes':
    
        mini()
        
    elif expense.lower() == 'no':
        print("thanks for using my progame")
        break
    else:
        print('please enter a valid choice')

            

    



    
